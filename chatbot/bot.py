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

    def __init__(self, group_id, token, ):
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
        if handler(text=text, context=state.context):
            next_step = steps[step['next_step']]
            if step['handler'] == 'handle_point_2' and state.context['point_2'] not in settings.SCHEDULE_CONFIG[
                state.context['point_1']]:
                next_step = steps['step9']
                text_to_send = next_step['text'].format(**state.context)
            elif step['handler'] == 'handle_date':
                text_to_send = dispatcher.dispatcher(state)
            elif step['handler'] == 'handle_comment':
                text_to_send = dispatcher.choose_ticket(state)
            elif step['handler'] == 'handle_choice' and state.context['choice'] == '0':
                next_step = steps['step10']
                text_to_send = next_step['text'].format(**state.context)
            elif step['handler'] == 'handle_email':
                if state.context['email'] == 'нет':
                    next_step = steps['step10']
                    text_to_send = next_step['text'].format(**state.context)
                else:
                    text_to_send = dispatcher.final(state)
            else:
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
    def __init__(self):
        self.flight_list = []

    def dispatcher(self, state):
        date_now = datetime.datetime.now()
        flight_date = datetime.datetime.strptime(state.context['out_date'], '%d-%m-%Y')
        self.city_out = state.context['point_1']
        self.city_in = state.context['point_2']
        flight_index = 0
        flight_date_span = []
        shift = datetime.timedelta(days=45)
        step = datetime.timedelta(days=1)
        flight_date_start = flight_date - shift
        flight_date_finish = flight_date + shift
        flight_ticket_span = []
        span_date_1 = flight_date
        flight_date_time = None
        flight_inform = ''
        day_shift = 2

        while flight_date_start < flight_date_finish:
            flight_date_span.append(flight_date_start)
            flight_date_start += step

        for span_date in flight_date_span:
            week_day = span_date.weekday()
            for day in settings.SCHEDULE_CONFIG[self.city_out][self.city_in].keys():
                if (type(day) is int and day == week_day) or (type(day) is not int and int(day) == span_date.day):
                    for number, item in \
                            settings.SCHEDULE_CONFIG[state.context['point_1']][state.context['point_2']][
                                day].items():
                        span_date_time = (datetime.datetime.combine(span_date.date(),
                                                                    datetime.datetime.strptime(item[0],
                                                                                               '%H.%M').time()))
                        arrival_time = datetime.datetime.strptime(item[1], '%H.%M').time()
                        flight_ticket_span.append([span_date_time, arrival_time, number])
                        if span_date == flight_date or (span_date_1 < flight_date and span_date > flight_date):
                            if not flight_date_time:
                                flight_date_time = span_date_time
                            if not flight_index:
                                flight_index = flight_ticket_span.index([span_date_time, arrival_time, number])
                            else:
                                continue
                        span_date_1 = span_date

        for value in (flight_ticket_span[flight_index - day_shift:flight_index + (5 - day_shift)]):
            if (flight_date.timestamp() - value[0].timestamp()) < (
                    flight_date.timestamp() - date_now.timestamp() - 3600):
                break
            else:
                day_shift -= 1
        self.flight_list = flight_ticket_span[(flight_index - day_shift):(flight_index + (5 - day_shift))]
        for number, item in enumerate(self.flight_list):
            string = f'{number + 1}. Номер рейса {item[2]}. Вылет {item[0].strftime("%d.%m.%Y")} в {item[0].strftime("%H.%M")}.\n'
            flight_inform += (string)
        flight_text = f'Предлагается список вылетов  по направлению {self.city_out.upper()} - ' \
                      f'{self.city_in.upper()}, наиболее близких по времени к' \
                      f' указанной дате. Выберите, пожалуйста, порядковый номер желаемого вылета из предлагаемого списка. ' \
                      f'Если Вам не подходит ни один рейс, выберите 0:\n' \
                      f'{flight_inform}' \

        return flight_text

    def choose_ticket(self, state):
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

        result_offer = f'Выбран{ending_1} {quantity} билет{ending_2} на рейс по маршруту {self.city_out.upper()}-{self.city_in.upper()}.\n' \
                       f' Рейс {flight_number}. Вылет {self.flight_list[int(choice) - 1][0].strftime("%d.%m.%Y")}' \
                       f' в {self.flight_list[int(choice) - 1][0].strftime("%H.%M")}. Прибытие в конечный пункт в' \
                       f' {self.flight_list[int(choice) - 1][1].strftime("%H.%M")}.\n' \
                       f' Если Вы согласны с предложением, напишите свой адрес электронной почты или телефон' \
                       f' для связи с оператором. Если не согласны, напишите "нет".' \

        return result_offer

    def final(self, state):
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


if __name__ == '__main__':
    dispatcher = Dispatcher()
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN, )
    bot.run()