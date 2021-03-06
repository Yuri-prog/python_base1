# -*- coding: utf-8 -*-

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

point = sd.get_point(50, 150)
def triangle(point, angle, length):

    v1 = sd.get_vector(start_point=point, angle=angle, length=length,)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+120,length=length,)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle+240, length=length,)
    v3.draw()
triangle(point, angle=30, length=200)

point = sd.get_point(250, 150)
def square(point, angle, length):                                                        

    v1 = sd.get_vector(start_point=point, angle=angle, length= length,)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+90,length=length,)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle+180, length= length,)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle+270, length=length,)
    v4.draw()
square(point, angle=0, length=200)

point = sd.get_point(530, 150)
def pentagon(point, angle, length):

     v1 = sd.get_vector(start_point=point, angle=angle, length=length,)
     v1.draw()
     v2 = sd.get_vector(start_point=v1.end_point, angle=angle+72,length=length,)
     v2.draw()
     v3 = sd.get_vector(start_point=v2.end_point, angle=angle+144, length= length,)
     v3.draw()
     v4 = sd.get_vector(start_point=v3.end_point, angle=angle+216, length=length,)
     v4.draw()
     v5= sd.get_vector(start_point=v4.end_point, angle=angle+288, length=length,)
     v5.draw()

pentagon(point, angle=0, length=140)

point = sd.get_point(790, 150)
def hexagon(point, angle, length):

     v1 = sd.get_vector(start_point=point, angle=angle, length=length,)
     v1.draw()
     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60,length=length,)
     v2.draw()
     v3 = sd.get_vector(start_point=v2.end_point, angle=angle+120, length=length,)
     v3.draw()
     v4 = sd.get_vector(start_point=v3.end_point, angle=angle+180, length=length,)
     v4.draw()
     v5 = sd.get_vector(start_point=v4.end_point, angle=angle+240, length=length,)
     v5.draw()
     v6 = sd.get_vector(start_point=v5.end_point, angle=angle+300, length=length,)
     v6.draw()

hexagon(point, angle=0, length=120)



# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

point = sd.get_point(530, 150)
first_point = point


def common(n):
    common_angle = 360/n
    return common_angle


def figure(n, angle, point,  length):
    for i in range(n):
        if i < n - 1:
            v = sd.get_vector(start_point=point, angle=angle+i*common(n), length=length, )
            point = v.end_point
            v.draw()
        else:
            v = sd.line(start_point=point, end_point=first_point)





figure(3, 0, point, 150)

sd.pause()

# зачет!
