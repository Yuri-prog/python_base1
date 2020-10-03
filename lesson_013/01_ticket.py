# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import argparse

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

def make_ticket(surname, initials, from_, to, date):

    ticket_name = 'images\\ticket_template.png'
    ticket = Image.open(ticket_name)
    print(ticket.format, ticket.size, ticket.mode)
    draw = ImageDraw.Draw(ticket)
    font = ImageFont.truetype('fonts\\Aqum.ttf', size=(ticket.size[1]//27))
    fio = str(surname+' '+initials)
    draw.text((ticket.size[0] / 13.44, ticket.size[1] / 3.21), fio, font=font, fill='black')
    draw.text((ticket.size[0] / 13.44, ticket.size[1] / 2.056), from_, font=font, fill='black')
    draw.text((ticket.size[0] / 13.44, ticket.size[1] / 1.54), to, font=font, fill='black')
    draw.text((ticket.size[0] / 2.6, ticket.size[1] / 1.54), date, font=font, fill='black')
    save_to = 'c:\\Users\\asus\\PycharmProjects\\python_base1\\lesson_013\\filled_ticket.png'
    ticket.save(save_to)



# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
parser = argparse.ArgumentParser(description='Запуск из командной строки: python файл surname initials from to date')
parser.add_argument('surname', type=str, help='Фамилия пассажира')
parser.add_argument('initials', type=str, help='Инициалы пассажира')
parser.add_argument('from_', type=str, help='Пункт вылета')
parser.add_argument('to', type=str, help='Пункт назначения')
parser.add_argument('date', type=str, help='Дата вылета')
parser.add_argument('--save_to', type=str, help='Путь сохранения файла')
args = parser.parse_args()
print(args.surname)
make_ticket(args.surname, args.initials, args.from_, args.to, args.date)

# зачет! 
