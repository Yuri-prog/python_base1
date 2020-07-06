# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd



N = 10

x_list = []
y_list = []
size_list = []
speed_list = []

# color = ''
colors = {
    'красный': sd.COLOR_RED,
    'оранжевый': sd.COLOR_ORANGE,
    'желтый': sd.COLOR_YELLOW,
    'зеленый': sd.COLOR_GREEN,
    'голубой': sd.COLOR_CYAN,
    'синий': sd.COLOR_BLUE,
    'фиолетовый': sd.COLOR_PURPLE,
    'разный': sd.random_color,
    'фон': sd.background_color,
    'белый': sd.COLOR_WHITE,
}
cl = colors['красный']


def flake():
    for i in range(0, N):
        k = sd.random_number(0, sd.resolution[0])
        x_list.insert(i, k)
        k = sd.random_number(sd.resolution[1] - 100, sd.resolution[1])
        y_list.insert(i, k)
        k = sd.random_number(10, 100)
        size_list.insert(i, k)
        size = size_list[i]

        sd.snowflake(center=sd.get_point(x=x_list[i], y=y_list[i]), length=size, )
#flake()
# rainbow(500, 60, radius=400)
sd.pause()
# зачет!
