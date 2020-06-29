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