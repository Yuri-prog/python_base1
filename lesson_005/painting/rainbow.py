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
#sd.pause()
# зачет!
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (1600, 800)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450
# start_step = 50
# end_step =350
# for color in rainbow_colors:
#     sd.line(sd.get_point(start_step, 50), sd.get_point(end_step, 450) , color=color, width=4)
#     start_step += 4
#     end_step += 4
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
def rainbow(x, y, radius):

    for color in rainbow_colors:
        center_position = sd.get_point(x, y)
        sd.circle(center_position=center_position, radius=radius, color = color, width = 20)
        radius += 20

#rainbow(500, 60, radius=400)
#sd.pause()
# зачет!