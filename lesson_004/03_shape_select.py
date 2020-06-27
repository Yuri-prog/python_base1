# -*- coding: utf-8 -*-

import simple_draw as sd



# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
center = sd.get_point(300, 300)
point_1 = sd.get_point(300-100, 300-int(200*(3**(0.5))/4))
point_2 = sd.get_point(300-100, 300-100)
point_3 = sd.get_point(300-70, 300-1.539*140/2)
point_4 = sd.get_point(300-60, 300-120*(3**(0.5)/2))


def triangle(point_1, angle, color, length):
    v1 = sd.get_vector(start_point=point_1, angle=angle, length=length, )
    l1 = sd.line(start_point=point_1, end_point=v1.end_point, color=color, width=1)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, )
    l2 = sd.line(start_point=v1.end_point, end_point=v2.end_point, color=color, width=1)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, )
    l3 = sd.line(start_point=v2.end_point, end_point=v3.end_point, color=color, width=1)


def square(point_2, angle, color, length):
    v1 = sd.get_vector(start_point=point_2, angle=angle, length=length, )
    l1 = sd.line(start_point=point_2, end_point=v1.end_point, color=color, width=1)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, )
    l2 = sd.line(start_point=v1.end_point, end_point=v2.end_point, color=color, width=1)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, )
    l3 = sd.line(start_point=v2.end_point, end_point=v3.end_point, color=color, width=1)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, )
    l4 = sd.line(start_point=v3.end_point, end_point=v4.end_point, color=color, width=1)


def pentagon(point_3, angle, color, length):
    v1 = sd.get_vector(start_point=point_3, angle=angle, length=length, )
    l1 = sd.line(start_point=point_3, end_point=v1.end_point, color=color, width=1)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, )
    l2 = sd.line(start_point=v1.end_point, end_point=v2.end_point, color=color, width=1)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, )
    l3 = sd.line(start_point=v2.end_point, end_point=v3.end_point, color=color, width=1)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, )
    l4 = sd.line(start_point=v3.end_point, end_point=v4.end_point, color=color, width=1)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, )
    l5 = sd.line(start_point=v4.end_point, end_point=v5.end_point, color=color, width=1)


def hexagon(point_4, angle, color, length):
    v1 = sd.get_vector(start_point=point_4, angle=angle, length=length, )
    l1 = sd.line(start_point=point_4, end_point=v1.end_point, color=color, width=1)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, )
    l2 = sd.line(start_point=v1.end_point, end_point=v2.end_point, color=color, width=1)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, )
    l3 = sd.line(start_point=v2.end_point, end_point=v3.end_point, color=color, width=1)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, )
    l4 = sd.line(start_point=v3.end_point, end_point=v4.end_point, color=color, width=1)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, )
    l5 = sd.line(start_point=v4.end_point, end_point=v5.end_point, color=color, width=1)
    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, )
    l6 = sd.line(start_point=v5.end_point, end_point=v6.end_point, color=color, width=1)


figures = ['Треугольник', 'Квадрат', 'Пятиугольник', 'Шестиугольник',]
for number, val in enumerate(figures, 1):

    print(number, val)

number = int(input('Введите номер фигуры'))
if number == 1:
    triangle(point_1, angle=0, color=sd.COLOR_YELLOW,length=200)
elif number == 2:
    square(point_2, angle=0, color=sd.COLOR_YELLOW, length=200)
elif number == 3:
    pentagon(point_3, angle=0, color=sd.COLOR_YELLOW, length=140)
elif number == 4:
    hexagon(point_4, angle=0, color=sd.COLOR_YELLOW, length=120)
else:
    print('Неверный ввод, повторите, пожалуйста')
sd.pause()
