#!/usr/bin/env python3
import datetime
from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock

from pony.orm import db_session, rollback
from vk_api.bot_longpoll import VkBotMessageEvent

import settings
from bot import Bot


def isolate_db(test_func):
    def wrapper(*args, **kwargs):
        with db_session:
            test_func(*args, **kwargs)
            rollback()

    return wrapper


class Test1(TestCase):
    RAW_EVENT = {
        'type': 'message_new',
        'object': {
            'message': {
                'date': 1603015285, 'from_id': 617520269, 'id': 462, 'out': 0, 'peer_id': 617520269,
                'text': 'привет бот', 'conversation_message_id': 461, 'fwd_messages': [], 'important': False,
                'random_id': 0, 'attachments': [], 'is_hidden': False},
            'client_info': {
                'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link'],
                'keyboard': True, 'inline_keyboard': True, 'lang_id': 0}
        },
        'group_id': 199257675, 'event_id': 'd072e30b324be5f8813b665f5338ca6bf42101c1'}

    def test_run(self):
        count = 5
        obj = {'a': 1}
        events = [obj] * count  # [obj, obj, ...]
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.run()
                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    test_date_year = datetime.datetime.today().timetuple()[0] + 2
    test_date = f'01-02-{test_date_year}'

    INPUTS = [
        'Привет',
        'справка',
        'купить',
        '/',
        'рим',
        'прага',
        'нью-йорк',
        str(test_date),
        '2',
        '2',
        'нет',
        'email@email.ru'
    ]

    x = (
        f' Предлагается список вылетов по направлению РИМ - НЬЮ-ЙОРК, наиболее близких по времени к указанной дате. Выберите,'
        f' пожалуйста, порядковый номер желаемого вылета из предлагаемого списка. Если Вам не подходит ни один рейс, выберите 0:\n'
        f'1. Номер рейса AF9742. Вылет 14.01.{test_date_year} в 09.30.\n'
        f'2. Номер рейса AF9742. Вылет 28.01.{test_date_year} в 09.30.\n'
        f'3. Номер рейса AF9742. Вылет 01.02.{test_date_year} в 09.30.\n'
        f'4. Номер рейса AF9742. Вылет 14.02.{test_date_year} в 09.30.\n'
        f'5. Номер рейса AF9742. Вылет 28.02.{test_date_year} в 09.30.\n')

    y = (
        f'Выбрано 2 билета на рейс по маршруту РИМ-НЬЮ-ЙОРК.\n Рейс AF9742. Вылет 28.01.{test_date_year} в 09.30. Прибытие в конечный пункт в 19.20.\n '
        f'Если Вы согласны с предложением, напишите свой адрес электронной почты или телефон для связи с оператором. Если не согласны, напишите "нет".')

    z = (
        'В ближайшее время с Вами свяжется специалист по электронной почте email@email.ru для окончательного оформления билета. Всего хорошего! До свидания!')

    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.TICKETS_INTENTS[0]['answer'],
        settings.TICKETS_INTENTS[1]['answer'],
        settings.TICKET_SCENARIOS['purchase']['steps']['step1']['text'],
        settings.TICKET_SCENARIOS['purchase']['steps']['step2']['text'],
        settings.TICKET_SCENARIOS['purchase']['steps']['step2']['failure_text'],
        settings.TICKET_SCENARIOS['purchase']['steps']['step3']['text'],
        settings.TICKET_SCENARIOS['purchase']['steps']['step4']['text'].format(dispatcher=x),
        settings.TICKET_SCENARIOS['purchase']['steps']['step5']['text'],
        settings.TICKET_SCENARIOS['purchase']['steps']['step6']['text'],
        settings.TICKET_SCENARIOS['purchase']['steps']['step7']['text'].format(choose_ticket=y),
        settings.TICKET_SCENARIOS['purchase']['steps']['step8']['text'].format(final=z),
    ]

    @isolate_db
    def test_run_ok(self):
        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event['object']['message']['text'] = input_text
            events.append(VkBotMessageEvent(event))
        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch('bot.VkBotLongPoll', return_value=long_poller_mock):
            bot = Bot('', '')
            bot.api = api_mock
            bot.run()

        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])

        assert real_outputs == self.EXPECTED_OUTPUTS
