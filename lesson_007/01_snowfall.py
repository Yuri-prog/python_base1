# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint, choice

sd.resolution = (1200, 600)
from lesson_006.snowfall import flake, color_and_list, move_right, move_left, count, short, flake_del


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    pass

    def __init__(self):
        self.length = randint(10, 100)
        self.x = randint(0, 1200)
        self.y = randint(500, 600)
        self.shift_y = randint(5, 15)
        self.shift_x = randint(-5, 5)

        self.count = count

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

    def get_flakes(self, count):
        flakes = []
        for i in range(0, N):
            i = Snowflake()
            flakes.append(i)
        return flakes

    # def get_fallen_flakes(self):
    #     if self.y > 0:



flake = Snowflake()

# k = 0
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

N = 30

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = Snowflake()
flakes = flakes.get_flakes(count=N)  # создать список снежинок

k = 0
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    k += 1
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


sd.pause()
