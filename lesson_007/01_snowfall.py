# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    pass  # TODO это не нужно

    def __init__(self):
        self.length = randint(10, 100)
        self.x = randint(0, 1200)
        self.y = randint(700, 900)
        self.shift_y = randint(5, 15)
        self.shift_x = randint(-5, 5)

    def draw(self):
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=sd.COLOR_WHITE)

    def clear_previous_picture(self):
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=sd.background_color)

    def move(self):
        self.y -= self.shift_y
        if k % 2 == 0:
            self.x -= self.shift_x
        else:
            self.x += self.shift_x

    def can_fall(self):
        if self.y > 0:
            return True

# TODO в классе Снежинка должны быть методы, относящиеся ТОЛЬКО к одной снежинке. Через неё нельзя получить все

    def get_flakes(self, count):
        flakes = []
        for i in range(count):
            i = Snowflake()
            flakes.append(i)
        return flakes

    def get_fallen_flakes(self):
        fallen_flakes = []
        for i in range(N):
            if self.y < 500:
                fallen_flakes.append(i)
        if len(fallen_flakes) >= N:
            return len(fallen_flakes)

    def append_flakes(self, count):
        for i in range(count):  # NOTE так тоже можно
            i = Snowflake()
            flakes.append(i)


flake = Snowflake()

# k = 0                                  #шаг 1
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#          break
#     k += 1
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

N = 15

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

flakes = Snowflake()
flakes = flakes.get_flakes(count=N)  # создать список снежинок
k = 0
fallen_flakes = 0
while True:
    sd.start_drawing()
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        fallen_flakes = flake.get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        flake.append_flakes(count=fallen_flakes)  # добавить еще сверху
    k += 1
    sd.sleep(0.1)
    sd.finish_drawing()
    if sd.user_want_exit():
        break

sd.pause()
