# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


start_point = sd.get_point(300, 50)
def draw_branches(start_point, angle, length):

    start_point_1 = start_point
    start_point_2 = start_point
    angle_1 = angle
    angle_2 = angle
    while length >= 10:
        v1 = sd.get_vector(start_point = start_point_1, angle = angle_1, length = length, width = 1)
        v2 = sd.get_vector(start_point = start_point_2, angle = angle_2, length = length, width = 1)
        length = 0.6*length
        start_point_1 = v1.end_point
        start_point_2 = v2.end_point
        angle_1 += 30
        angle_2 -= 30
        v1.draw()
        v2.draw()


#draw_branches(start_point, 90, 150)

root_point = sd.get_point(300, 30)
def draw_branches(start_point, angle, length, delta):
    if length < 10:
       return
    v1 = sd.get_vector(start_point, angle=angle, length=length,)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle + delta
    next_length = 0.75 * length
    draw_branches(start_point=next_point, angle=angle+delta, length=next_length, delta=delta)
    draw_branches(start_point=next_point, angle=angle-delta, length=next_length, delta=delta)

#draw_branches(start_point=root_point, angle = 90, length = 100, delta = 30)


#Усложненное задание

delta = 0


def draw_branches(start_point, angle, length, delta):
    if length < 2:
        return
    v1 = sd.get_vector(start_point, angle=angle, length=length,)
    v1.draw()
    next_point = v1.end_point
    x = int(30 / 100 * 40)
    y = int(length / 100 * 20)
    length = sd.random_number(length - y, length + y)
    delta = sd.random_number(30 - x, 30 + x)
    next_angle = angle + delta
    next_length = int(0.75 * length)
    draw_branches(start_point=next_point, angle=angle + delta, length=next_length, delta=delta,)
    draw_branches(start_point=next_point, angle=angle - delta, length=next_length, delta=delta,)


draw_branches(start_point=root_point, angle=90, length=100, delta=delta)




# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


