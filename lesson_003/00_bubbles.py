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
for j in range(100, 1001, 100):
    rad = 50
    center = sd.get_point(j, 300)
    for i in range(3):
      sd.circle(center, radius=rad)
      rad = rad + 5


# Нарисовать три ряда по 10 пузырьков
for x in range(100, 301,100):
   for j in range(100, 1001, 100):
     rad = 50
     center = sd.get_point(j, x)
     for i in range(3):
        sd.circle(center, radius=rad)
        rad = rad + 5

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    bubble(point, 3, 3, color)


sd.pause()


