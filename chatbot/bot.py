#!/usr/bin/env python3
import vk_api
import random
#from _token import token, group_id
from vk_api import bot_longpoll, VkApi
import requests
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll, VkBotMessageEvent
import logging
try:
    import settings
except ImportError:
    exit('Do cp settings.py.default settings.py and set token.')

log = logging.getLogger('bot')

def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler('bot.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%d-%m-%Y %H:%M'))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)

    log.setLevel(logging.DEBUG)

configure_logging()

# class Trading:
#     def __init__(self):
#         self.sent_message = ''
#
#     def respond(self):
#         if bot.received_message:
#             print(bot.received_message)
#             self.sent_message = 'Здравствуйте. Имеются в продаже прохладительные напитки. Не желаете приобрести? Если да, введите 1, нет - введите 0.'
#         else:
#             self.sent_message = 'Сам дурак'
#         print(self.sent_message)




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
        self.vk  = VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()
        self.received_message = ''
        self.server = ''

    def run(self):
        """Запуск бота"""
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('Ошибка в обработке события')
        print(self.received_message)
    def on_event(self, event):
        """Отправляет сообщение назад, если это текст
        :param event: VkBotMessageEvent object
        :return: None
        """
        # data = self.vk.method('groups.getLongPollServer', {'group_id': 199257675})
        # print(data)

        # while True:
        # response = requests.get(
        #     '{server}?act=a_check&key={key}&wait=25&mode=2&ts={ts}'.format(server=data['server'], key=data['key'], ts=data['ts'])).json()
        # print(response)

        if event.type == VkBotEventType.MESSAGE_NEW:
            #print(self.received_message)
            self.received_message = event.object.message['text']
            log.debug('Отправляем сообщение назад')
            print(self.received_message)
            print(event)


        #trading.respond()
        #print(event)
        #print(self.vk.method('users.get', {'user_ids': event.message.peer_id, 'fields': 'photo_50, city, sex'}))
            self.api.messages.send(message=self.received_message,
                                   random_id=random.randint(0, 2**20),
                                   peer_id=event.message.peer_id)
        else:
            log.info('Пока не умеем обрабатывать %s', event.type)

        #     self.api.messages.send(message='Жопа', random_id=random.randint(0, 2 ** 20), peer_id=event.object.peer_id)


if __name__ == '__main__':
    #trading = Trading()
    bot = Bot(settings.group_id, settings.token)
    bot.run()
    #forward_messages = 'здоров',
