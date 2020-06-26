# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

import simple_draw as sd

sd.resolution = (1200, 600)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
point_1 = sd.get_point(50, 150)
point_2 = sd.get_point(250, 150)
point_3 = sd.get_point(530, 150)
point_4 = sd.get_point(790, 150)


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


colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
russian_colors = ['Красный', 'Оранжевый', 'Желтый', 'Зеленый', 'Голубой', 'Синий', 'Фиолетовый']

for figure_color, val in enumerate(russian_colors):
    print(figure_color, val)

print('Выберите  цвет фигуры треугольник')
figure_color = int(input())
if 0 <= figure_color <= 5:
    triangle(point_1, angle=30, color=colors[figure_color], length=200)
else:
    print('Неверный выбор, введите заново')
print('Выберите  цвет фигуры квадрат')
figure_color = int(input())
if 0 <= figure_color <= 5:
    square(point_2, angle=0, color=colors[figure_color], length=200)
else:
    print('Неверный выбор, введите заново')
print('Выберите  цвет фигуры пятиугольник')
figure_color = int(input())
if 0 <= figure_color <= 5:
    pentagon(point_3, angle=0, color=colors[figure_color], length=140)
else:
    print('Неверный выбор, введите заново')

print('Выберите  цвет фигуры шестиугольник')
figure_color = int(input())
if 0 <= figure_color <= 5:
    hexagon(point_4, angle=0, color=colors[figure_color], length=120)

else:
    print('Неверный выбор, введите заново')

sd.pause()
# зачет!