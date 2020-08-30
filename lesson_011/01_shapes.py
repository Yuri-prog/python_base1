# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def figure(point, angle, length):
        for i in range(n):
            i = sd.get_vector(start_point=point, angle=angle + (360 / n) * i, length=length, )
            i.draw()
            point = i.end_point

    return figure


draw_triangle = get_polygon(n=5)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
