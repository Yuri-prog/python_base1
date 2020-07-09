# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)

N = 50

x_list = []
y_list = []
size_list = []
speed_list = []
shift_x_list = []
shift_y_list = []
x = 0
y = 0

colors = {
    'красный': sd.COLOR_RED,
    'оранжевый': sd.COLOR_ORANGE,
    'желтый': sd.COLOR_YELLOW,
    'зеленый': sd.COLOR_GREEN,
    'голубой': sd.COLOR_CYAN,
    'синий': sd.COLOR_BLUE,
    'фиолетовый': sd.COLOR_PURPLE,
    'фон': sd.background_color,
    'белый': sd.COLOR_WHITE,
}
cl = colors['белый']

for i in range(0, N):
    k = sd.random_number(0, sd.resolution[0])
    x_list.insert(i, k)
    k = sd.random_number(sd.resolution[1] - 100, sd.resolution[1])
    y_list.insert(i, k)
    k = sd.random_number(10, 100)
    size_list.insert(i, k)
    k = sd.random_number(-5, 5)
    shift_x_list.insert(i, k)
    k = sd.random_number(5, 15)
    shift_y_list.insert(i, k)


def flake():
    global x, y, size, shift_x, shift_y

    sd.snowflake(center=sd.get_point(x_list[i], y_list[i]), length=size_list[i], color=cl)

def color(color):
    global cl, i
    for i in range(0, N):
        cl = colors[color]
        flake()
        #print(y_list[1])
#flake()

def move():
    for i in range(0, N):
       x_list[i] += shift_x_list[i]
       y_list[i] -= shift_y_list[i]

      # print(y_list[1])







#sd.pause()
