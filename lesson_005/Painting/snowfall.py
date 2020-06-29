# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

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

x_list = []
y_list = []



for x in range(0, N - 1):
    k = sd.random_number(0, 300)
    x_list.insert(x, k)

for y in range(0, N - 1):
    k = sd.random_number(600, 800)
    y_list.insert(y, k)



def for_painting(length):
    x_list = []
    y_list = []
    N = 50

    for x in range(0, N - 1):
        k = sd.random_number(0, 300)
        x_list.insert(x, k)

    for y in range(0, N - 1):
        k = sd.random_number(600, 800)
        y_list.insert(y, k)

    for i in range(N - 1):
        x = x_list[i]
        y = y_list[i]

        while True:
            sd.start_drawing()
            sd.snowflake(center=sd.get_point(x, y), length=length, color=sd.background_color)

            y -= 20

            sd.snowflake(center=sd.get_point(x, y), length=length, color=sd.COLOR_WHITE)

            sd.sleep(0.005)

            if 0 <= i < N - 30:
                if y < 75:
                    y = 70
                    break
            elif N - 30 <= i < N - 20:
                if y < 95:
                    y = 90
                    break
            elif N - 20 <= i < N - 12:
                if y < 111:
                    y = 110
                    break
            elif N - 12 <= i < N - 5:
                if y < 121:
                    y = 120
                    break
            elif N - 5 <= i < N:
                if y < 141:
                    y = 140
                    break
            sd.finish_drawing()
            if sd.user_want_exit():
                break

#for_painting(20)
#sd.pause()


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
