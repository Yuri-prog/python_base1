# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw
simple_draw.resolution = (1200, 600)

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x_center, y_center, color):

    x1 = x_center-100
    y1 = y_center-75
    x2 = x_center+100
    y2 = y_center+75
    left_bottom = simple_draw.get_point(x1, y1)
    right_top = simple_draw.get_point(x2, y2)
    eye_center_1 = simple_draw.get_point(x1+0.3*(x2-x1), y1+0.6*(y2-y1))
    eye_center_2 = simple_draw.get_point(x1 + 0.7 * (x2 - x1), y1 + 0.6 * (y2 - y1))
    radius = 0.05*(x2-x1)
    simple_draw.ellipse(left_bottom, right_top, color, width=2)          #лицо
    simple_draw.circle(eye_center_1, radius, color, width=2)             #левый глаз
    simple_draw.circle(eye_center_2, radius, color, width=2)             #правый глаз

    for angle in range (200, 340,):
        mouth_point = simple_draw.get_point(simple_draw.cos(angle) * 50 + x_center,
                                            simple_draw.sin(angle) * 30 + y_center - 15, )
        simple_draw.circle(mouth_point, 0.1 * radius, color)             #рот



for i in range(10):

    x_center = simple_draw.random_number(0, 1100)
    y_center = simple_draw.random_number(0, 600)
    color = simple_draw.random_color()
    smile(x_center, y_center, color)

simple_draw.pause()
# зачет!