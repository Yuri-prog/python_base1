# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd



def smile(x, y, color):
    point1 = sd.get_point(x=x, y=y)
    point2 = sd.get_point(x=x + 100, y=y + 70)
    sd.ellipse(point1, point2, width=0, color=sd.COLOR_YELLOW)
    point3 = sd.get_point(x=x + 33, y=y + 45)
    sd.circle(point3, radius=5, color=color)
    point4 = sd.get_point(x=x + 66, y=y + 45)
    sd.circle(point4, radius=5, color=color)
    p5 = sd.get_point(x+40, y+20)
    p6 = sd.get_point(x+60, y+20)
    sd.line(p5, p6, color=color)
    p7 = sd.get_point(x+20, y+30)
    sd.line(p7, p5, color=color)
    p8 = sd.get_point(x+80, y+30)
    sd.line(p6, p8, color=color)


# for i in range(10):
#     x = sd.random_number(10, 500)
#     y = sd.random_number(10, 500)
#smile(100, 200, sd.COLOR_GREEN)

#sd.pause()
