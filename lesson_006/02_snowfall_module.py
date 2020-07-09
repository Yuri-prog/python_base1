# -*- coding: utf-8 -*-
import simple_draw as sd
import probe1

sd.resolution = (1200, 600)

#TODO: В таком виде программа не запускается, выдает такую ошибку. File "D:\Python\lib\site-packages\simple_draw-2.6.8-py3.8.egg\simple_draw.py", line 437, in snowflake
# pygame.error: video system not initialized. Функция flake() в модуле запускается нормально.


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

probe1.flake()

while True:
    sd.start_drawing()

    probe1.color('фон')
    probe1.move()
    probe1.color('белый')


    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)

    sd.sleep(0.01)
    sd.finish_drawing()

    # if sd.user_want_exit():
    #     break
sd.pause()
