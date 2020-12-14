'''Handler - функция, принимающая на вход текст входящего сообщения и context(dict), а возвращает bool, пройден шаг или нет'''
import datetime
import re

import settings
#from bot import dispatcher
import bot


re_email = re.compile(r'\b[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+\b')
re_phone = re.compile(r'\W*\d\W*\W*\d\d\d\W*\W*\d\d\d\W*\d\d\W*\d\d')
re_number = re.compile(r'\b[1-2]\b')
re_quantity = re.compile(r'\b[1-5]\b')
re_date = re.compile(r'\b(0[1-9]|1[0-9]|2[0-9]|3[0-1])-(0[1-9]|1[1-2])-20[2-9]\d\b')
re_choice = re.compile(r'\b[0-5]\b')
city_list = ['москва', 'санкт-петербург', 'лондон', 'париж', 'рим', 'берлин', 'барселона', 'нью-йорк']


def handle_point_1(text, context, state):
    for match in city_list:
        if match in text.lower():
            context['point_1'] = text.lower()
            return True
        else:
            continue


def handle_point_2(text, context, state):
    for match in city_list:
        if match in text.lower():
            context['point_2'] = text.lower()
            if text.lower() in settings.SCHEDULE_CONFIG[context['point_1']]:
                return True
            else:
                return 'step9'
        else:
            continue


def handle_email(text, context, state):
    matches = re.findall(re_email, text)
    matches1 = re.findall(re_phone, text)
    if matches:
        context['email'] = text
        context['final'] = bot.dispatcher.final(state)
        return True
    elif matches1:
        context['email'] = text
        print(context['email'])
        context['final'] = bot.dispatcher.final(state)
        return True
    elif text == 'нет':
        context['email'] = text
        return 'step10'
    else:
        return False


def handle_quantity(text, context, state):
    match = re.match(re_quantity, text)
    if match:
        context['quantity'] = text
        return True
    else:
        return False


def handle_date(text, context, state):
    match = re.match(re_date, text)
    if match:
        if datetime.datetime.strptime(text, '%d-%m-%Y').date() >= datetime.date.today():
            context['out_date'] = text
            context['dispatcher'] = bot.dispatcher.dispatcher(state)
            return True
    else:
        return False

def handle_choice(text, context, state):
    match = re.match(re_choice, text)
    if match:
        context['choice'] = text
        if text == '0':
            return 'step10'
        else:
            return True
    else:
        return False


def handle_comment(text, context, state):
    context['comment'] = text
    context['choose_ticket'] = bot.dispatcher.choose_ticket(state)
    return True
