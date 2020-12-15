#!/usr/bin/env python3

import datetime
import vk_api
import random
from pony.orm import db_session
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import logging
import handlers
from models import UserState, Ticket

try:
    import settings
except ImportError:
    exit('Do cp settings.py.default settings.py and set token.')

log = logging.getLogger('bot')

def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler('bot.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%d-%m-%Y %H:%M'))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)

class Bot:
    """
    Echo bot лля vk.com
    Use python3.8
    """

    def __init__(self, group_id, token):
        """
        param group_id: group_id из vk
        param token: секретный ключ
        """
        self.group_id = group_id
        self.token = token
        self.vk = VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        """Запуск бота"""
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('Ошибка в обработке события')

    @db_session
    def on_event(self, event):
        """Отправляет сообщение назад, если это текст
        :param event: VkBotMessageEvent object
        :return: None
        """
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info('Пока не умеем обрабатывать %s', event.type)
            return

        user_id = event.object.message['peer_id']
        text = event.object.message['text']
        state = UserState.get(user_id=str(user_id))

        if state is not None:
            text_to_send = self.continue_scenario(text, state)

            # continue scenario
        else:
            # search intent
            for intent in settings.TICKETS_INTENTS:
                log.debug(f'User got {intent}')
                if any(token in text.lower() for token in intent['tokens']):
                    if intent['answer']:
                        text_to_send = intent['answer']
                    else:
                        text_to_send = self.start_scenario(user_id, intent['scenario'])
                    break
            else:
                text_to_send = settings.DEFAULT_ANSWER

        self.api.messages.send(message=text_to_send,
                               random_id=random.randint(0, 2 ** 20),
                               peer_id=user_id, )


    def start_scenario(self, user_id, scenario_name):
        scenario = settings.TICKET_SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        UserState(user_id=str(user_id), scenario_name=scenario_name, step_name=first_step, context={})
        return text_to_send

    def continue_scenario(self, text, state):
        steps = settings.TICKET_SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]
        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context, state=state):
            if type(handler(text=text, context=state.context, state=state)) is str:
                next_step = steps[handler(text=text, context=state.context, state=state)]
            else:
                next_step = steps[step['next_step']]

            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                state.step_name = step['next_step']
            else:
                if next_step == steps['step8']:
                    log.info('Оформлен билет {point_1}-{point_2} на рейс {flight_number} {out_date}.'.format(**state.context))
                    Ticket(city_out=state.context['point_1'], city_in=state.context['point_2'], flight_date=state.context['out_date'],
                           flight_number=state.context['flight_number'])
                else:
                    log.info('Билет не оформлен.'.format(**state.context))
                # finish scenario
                state.delete()
        else:
            text_to_send = step['failure_text'].format(**state.context)

        return text_to_send


class Dispatcher:
    """ Выдает клиенту список 5 вылетов на выбор
    """
    def __init__(self):
        self.flight_list = []
        self.flight_date = None
        self.flight_date_span = []
        self.flight_ticket_span = []
        self.flight_index = 0
        self.flight_text = ''

    def flights(self, state):
        span_date_1 = self.flight_date
        flight_date_time = None
        for span_date in self.flight_date_span:
            for day in settings.SCHEDULE_CONFIG[state.context['point_1']][state.context['point_2']].keys():
                if (type(day) is int and day == span_date.weekday()) or (
                        type(day) is not int and int(day) == span_date.day):
                    for number, item in \
                            settings.SCHEDULE_CONFIG[state.context['point_1']][state.context['point_2']][
                                day].items():
                        span_date_time = (datetime.datetime.combine(span_date.date(),
                                                                    datetime.datetime.strptime(item[0],
                                                                                               '%H.%M').time()))
                        arrival_time = datetime.datetime.strptime(item[1], '%H.%M').time()
                        self.flight_ticket_span.append([span_date_time, arrival_time, number])
                        if span_date == self.flight_date or (span_date_1 < self.flight_date and span_date > self.flight_date):
                            if not flight_date_time:
                                flight_date_time = span_date_time
                            if not self.flight_index:
                                self.flight_index = self.flight_ticket_span.index([span_date_time, arrival_time, number])
                            else:
                                continue
                        span_date_1 = span_date

    def flight_inform(self, state):
        day_shift = 2
        flight_inform = ''
        for value in (self.flight_ticket_span[self.flight_index - day_shift:self.flight_index + (5 - day_shift)]):
            if (self.flight_date.timestamp() - value[0].timestamp()) < (
                    self.flight_date.timestamp() - datetime.datetime.now().timestamp() - 3600):
                break
            else:
                day_shift -= 1
        self.flight_list = self.flight_ticket_span[(self.flight_index - day_shift):(self.flight_index + (5 - day_shift))]
        for number, item in enumerate(self.flight_list):
            string = f'{number + 1}. Номер рейса {item[2]}. Вылет {item[0].strftime("%d.%m.%Y")} в {item[0].strftime("%H.%M")}.\n'
            flight_inform += string

        self.flight_text = (f' Предлагается список вылетов по направлению {state.context["point_1"].upper()} - ' \
                      f'{state.context["point_2"].upper()}, наиболее близких по времени к' \
                      f' указанной дате. Выберите, пожалуйста, порядковый номер желаемого вылета из предлагаемого списка.' \
                      f' Если Вам не подходит ни один рейс, выберите 0:\n' \
                      f'{flight_inform}') \


    def dispatcher(self, state):
        self.flight_date = datetime.datetime.strptime(state.context['out_date'], '%d-%m-%Y')
        step = datetime.timedelta(days=1)
        flight_date_start = self.flight_date - datetime.timedelta(days=45)
        flight_date_finish = self.flight_date + datetime.timedelta(days=45)

        while flight_date_start < flight_date_finish:
            self.flight_date_span.append(flight_date_start)
            flight_date_start += step
        self.flights(state)
        self.flight_inform(state)
        return self.flight_text

    def choose_ticket(self, state):
        """ Обрабатывает выбор клиента и выдает конечный результат. Запрашивает контакты клиента.
        """
        quantity = state.context['quantity']
        choice = state.context['choice']
        flight_number = self.flight_list[int(choice) - 1][2]
        state.context['flight_number'] = flight_number
        if quantity == '2' or quantity == '3' or quantity == '4':
            ending_1 = 'о'
            ending_2 = 'а'
        if quantity == '5':
            ending_1 = 'о'
            ending_2 = 'ов'
        if quantity == '1':
            ending_1 = ''
            ending_2 = ''

        result_offer = f'Выбран{ending_1} {quantity} билет{ending_2} на рейс по маршруту {state.context["point_1"].upper()}' \
                       f'-{state.context["point_2"].upper()}.\n' \
                       f' Рейс {flight_number}. Вылет {self.flight_list[int(choice) - 1][0].strftime("%d.%m.%Y")}' \
                       f' в {self.flight_list[int(choice) - 1][0].strftime("%H.%M")}. Прибытие в конечный пункт в' \
                       f' {self.flight_list[int(choice) - 1][1].strftime("%H.%M")}.\n' \
                       f' Если Вы согласны с предложением, напишите свой адрес электронной почты или телефон' \
                       f' для связи с оператором. Если не согласны, напишите "нет".' \

        return result_offer

    def final(self, state):
        """ Финальное сообщение.
        """
        contact = state.context['email']
        if '@' in contact:
            phrase = 'электронной почте'
        elif contact == 'нет':
            return False
        else:
            phrase = 'телефону'
        final = f'В ближайшее время с Вами свяжется специалист по {phrase} {contact} для окончательного' \
                f' оформления билета. Всего хорошего! До свидания!'
        return final

dispatcher = Dispatcher()
if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN,)
    bot.run()