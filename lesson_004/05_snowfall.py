# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


x_list = []
y_list = []
size_list = []


for x in range(0, N - 1):
    k = sd.random_number(0, 1200)
    x_list.insert(x, k)

for y in range(0, N - 1):
    k = sd.random_number(500, 600)
    y_list.insert(y, k)

for j in range(0, N - 1):
    k = sd.random_number(10, 100)
    size_list.insert(j, k)

for i in range(0, N - 1):

    x0 = x_list[0]
    y0 = y_list[0]
    x1 = x_list[1]
    y1 = y_list[1]
    x2 = x_list[2]
    y2 = y_list[2]
    x3 = x_list[3]
    y3 = y_list[3]
    x4 = x_list[4]
    y4 = y_list[4]
    x5 = x_list[5]
    y5 = y_list[5]
    x6 = x_list[6]
    y6 = y_list[6]
    x7 = x_list[7]
    y7 = y_list[7]
    x8 = x_list[8]
    y8 = y_list[8]
    x9 = x_list[9]
    y9 = y_list[9]
    x10 = x_list[10]
    y10 = y_list[10]
    size0 = size_list[0]
    size1 = size_list[1]
    size2 = size_list[2]
    size3 = size_list[3]
    size4 = size_list[4]
    size5 = size_list[5]
    size6 = size_list[6]
    size7 = size_list[7]
    size8 = size_list[8]
    size9 = size_list[9]
    size10 = size_list[10]

    while True:
        point = sd.get_point(x=x0, y=y0)
        sd.clear_screen()
        sd.start_drawing()


        sd.snowflake(center=point, length=size0, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
        y0 -= 5
        point = sd.get_point(x=x1, y=y1)
        sd.snowflake(center=point, length=size1, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
        y1 -= 7
        point = sd.get_point(x=x2, y=y2)
        sd.snowflake(center=point, length=size2, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
        y2 -= 8
        point = sd.get_point(x=x3, y=y3)
        sd.snowflake(center=point, length=size3, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
        y3 -= 8
        point = sd.get_point(x=x4, y=y4)
        sd.snowflake(center=point, length=size4, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
        y4 -= 8
        point = sd.get_point(x=x5, y=y5)
        sd.snowflake(center=point, length=size5, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
        y5 -= 10

        if y0 <= 50:
            y0 = 50
            point = sd.get_point(x=x6, y=y6)
            sd.snowflake(center=point, length=size6, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
            y6 -= 7
        if y1 <= 50:
            y1 = 50
            point = sd.get_point(x=x7, y=y7)
            sd.snowflake(center=point, length=size7, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
            y7 -= 8
        if y2 <= 50:
            y2 = 50
            point = sd.get_point(x=x8, y=y8)
            sd.snowflake(center=point, length=size8, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
            y8 -= 8
        if y3 <= 50:
            y3 = 50
            point = sd.get_point(x=x9, y=y9)
            sd.snowflake(center=point, length=size9, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
            y9 -= 3
        if y4 <= 50:
            y4 = 50
            point = sd.get_point(x=x10, y=y10)
            sd.snowflake(center=point, length=size10, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
            y10 -= 4
        if y5 <= 50:
            y5 = 50
        if y6 <= 50:
            y6 = 50
        if y7 <= 50:
            y7 = 50
        if y8 <= 50:
            y8 = 50
        if y9 <= 50:
            y9 = 50
        if y10 <= 50:
            y10 = 50
        sd.finish_drawing()
        sd.sleep(0.02)

        if y6 == y7 == y8 == y9 == y10:
            break
        if sd.user_want_exit():
            break

sd.pause()



# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

