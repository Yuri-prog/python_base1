# -*- coding: utf-8 -*-
import simple_draw as sd
from snowfall import flake, color, move_right, move_left, count, short, flake_del

sd.resolution = (1200, 600)

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

flake()
k = 0
while True:
    sd.start_drawing()
    color('фон')
    if k%2 == 0:
        move_right()
    else:
        move_left()
    color('желтый')
    k += 1
    if count() == False:  # TODO: Проверку на False/True/None лучше выполнять с помощью оператора is.
        break
    sd.sleep(0.1)
    sd.finish_drawing()
    if sd.user_want_exit():
        break
    flake_del()

sd.pause()

