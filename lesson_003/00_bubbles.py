# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

 #Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
center = sd.get_point(300, 300)
rad = 100
for i in range(3):
  sd.circle(center, radius=rad)
  rad = rad + 5


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point, step, quantity, color):
    rad = 50
    for i in range(quantity):
      sd.circle(point, rad, color)
      rad = rad + step


#point = sd.get_point(200, 200)
#bubble(point, 5, 30, color=sd.COLOR_RED)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


