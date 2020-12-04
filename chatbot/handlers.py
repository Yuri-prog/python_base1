'''Handler - функция, принимающая на вход текст входящего сообщения и context(dict), а возвращает bool, пройден шаг или нет'''
import datetime
import re

from generate_ticket import generate_ticket

re_name = re.compile(r'^[\w\-\s]{3,40}$')
re_email = re.compile(r'\b[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+\b')
re_phone = re.compile(r'\W*\d\W*\W*\d\d\d\W*\W*\d\d\d\W*\d\d\W*\d\d')
re_number = re.compile(r'\b[1-2]\b')
re_quantity = re.compile(r'\b[1-5]\b')
re_date = re.compile(r'(0[1-9]|1[0-9]|2[0-9]|3[0-1])-(0[1-9]|1[1-2])-20[2-9]\d')#(r'\d\d-\d\d-\d\d\d\d')
re_choice = re.compile(r'\b[0-5]\b')
city_list = ['москва', 'санкт-петербург', 'лондон', 'париж', 'рим', 'берлин', 'барселона', 'нью-йорк']

# def handle_point_1(text, context):
#     match = re.match(re_name, text)
#     if match:
#         context['point_1'] = text
#         return True
#     else:
#         return False

def handle_point_1(text, context):
    for match in city_list:
        if match in text.lower():
            context['point_1'] = text.lower()
            #continue
            return True
        else:
            continue
            #return True

def handle_point_2(text, context):
    for match in city_list:
        if match in text.lower():
            context['point_2'] = text.lower()
            #continue
            return True
        else:
            continue



def handle_email(text, context):
    matches = re.findall(re_email, text)
    matches1 = re.findall(re_phone, text)
    if matches:
        context['email'] = text
        return True
    elif matches1:
        context['email'] = text
        return True
    elif text == 'нет':
        context['email'] = text
        return True
    else:
        return False

def generate_ticket_handler(text, context):
    return generate_ticket(name=context['name'], email=context['email'])

# def handle_number(text, context):
#     match = re.match(re_number, text)
#     if match:
#         context['number'] = text
#         return True
#     else:
#         return False

def handle_quantity(text, context):
    match = re.match(re_quantity, text)
    if match:
        context['quantity'] = text
        return True
    else:
        return False

def handle_date(text, context):
    match = re.match(re_date, text)
    if match:
        if datetime.datetime.strptime(text, '%d-%m-%Y').date() >= datetime.date.today():
            context['out_date'] = text
            return True
    else:
        return False

def handle_choice(text, context):
    match = re.match(re_choice, text)
    if match:
        context['choice'] = text
        return True
    else:
        return False

def handle_comment(text, context):
    context['comment'] = text
    return True

def handle_agreement(text, context):
    if text.lower() == 'да' or text.lower() == 'нет':
        context['agreement'] = text
        return True
    else:
        return False