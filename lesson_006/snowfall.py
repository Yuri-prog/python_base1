# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (1200, 600)

N = 30

x_list = []
y_list = []
size_list = []
speed_list = []
shift_x_list = []
shift_y_list = []
flake_numbers = []

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
    k = sd.random_number(5, 12)
    shift_y_list.insert(i, k)


def flake():
    global x, y, size, shift_x, shift_y
    sd.snowflake(center=sd.get_point(x_list[i], y_list[i]), length=size_list[i], color=cl)

def color(color):
    global cl, i
    for i in range(0, N):
        cl = colors[color]
        flake()

def move_right():
    for i in range(0, N):
        x_list[i] += shift_x_list[i]
        y_list[i] -= shift_y_list[i]


def move_left():
    for i in range(0, N):
        x_list[i] -= shift_x_list[i]
        y_list[i] -= shift_y_list[i]

def short(list):
    for m in list:
        if list.count(m) > 1:
            list.remove(m)
    print('За границу экрана вышли снежинки №', *list)

def count():
    for j, m in enumerate(y_list):
        if -20 < m < 0:
            flake_numbers.append(j)
    short(flake_numbers)

    if y_list[i] < -2000:
        return False

def flake_del():
 for j, m in enumerate(y_list):
    if -820 < m < -800:
        if flake_numbers.count(j) == 0:
            continue
        else:
            flake_numbers.remove(j)






#sd.pause()

