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
size_list =[]



for x in range(0, N-1):
    k = sd.random_number(0, 1200)
    x_list.insert(x, k)

for y in range(0, N-1):
    k = sd.random_number(500, 600)
    y_list.insert(y, k)

for j in range(0, N-1):
    k = sd.random_number(10, 100)
    size_list.insert(j, k)


for i in range(0, N-1):
    length = 0
    x = x_list[i]
    y = y_list[i]
    size = size_list[i]

    length = size
    point = sd.get_point(x=x, y=y)

    while True:
        sd.start_drawing()
        sd.snowflake(center=point, length=length, color=sd.COLOR_DARK_BLUE, factor_a=0.6, factor_b=0.35, factor_c=60)
        y -= 5
        point = sd.get_point(x=x+50, y=y)
        sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)

        sd.finish_drawing()
        sd.sleep(0.01)
        if y < 50:
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

