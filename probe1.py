# -*- coding: utf-8 -*-

import simple_draw as sd

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
sd.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 10

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

x_coords = []
y_coords = []
lengths = []

for x in range(0, SCREEN_WIDTH, SCREEN_WIDTH // N):
    x_coords.append(x)
    y_coords.append(sd.random_number(SCREEN_HEIGHT - 300, SCREEN_HEIGHT))
    lengths.append(sd.random_number(20, 40))

while True:
    sd.start_drawing()
    at_bottom_bound = sd.random_number(30, 70)
    for i, x in enumerate(x_coords):
        if y_coords[i] < at_bottom_bound:
            continue
        delta_y = sd.random_number(10, 20)
        if y_coords[i] - delta_y < at_bottom_bound:
            # если снежинка достигла дна, то перемещаем её наверх экрана.
            # а так как она в прошлом цикле была нарисована белым, то этот отпечаток останется в сугробе
            x_coords[i] = sd.random_number(0, SCREEN_WIDTH)
            y_coords[i] = sd.random_number(SCREEN_HEIGHT - 50, SCREEN_HEIGHT)
            lengths[i] = sd.random_number(20, 40)

        point = sd.get_point(x, y_coords[i])
        sd.snowflake(center=point, length=lengths[i], color=sd.background_color)

        x_coords[i] += sd.random_number(-30, 30)
        y_coords[i] -= delta_y

        point = sd.get_point(x_coords[i], y_coords[i])
        sd.snowflake(center=point, length=lengths[i])

    if max(y_coords) < 50:
        break

    sd.finish_drawing()
    sd.sleep(0.01)
    if sd.user_want_exit():
        break

sd.pause()


