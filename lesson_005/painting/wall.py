# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (1200, 600)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
def bricks(beg_length, end_length, beg_height, end_height, length_br, hight_br):
    for x in range(beg_length, end_length, length_br):

        for y in range(beg_height, end_height, hight_br):
            if y % length_br == 0:
                sd.rectangle(sd.get_point(x-length_br/2, y), sd.get_point(x + length_br/2, y + hight_br), color=sd.COLOR_YELLOW, width=1)
            else:
               sd.rectangle(sd.get_point(x, y), sd.get_point(x + length_br, y + hight_br), color=sd.COLOR_YELLOW, width=1)

    sd.line(start_point=sd.get_point(beg_length-length_br/2, beg_height), end_point=sd.get_point(beg_length-length_br/2,  end_height), color=sd.COLOR_YELLOW, width=1)
    sd.line(start_point=sd.get_point(end_length, beg_height), end_point=sd.get_point(end_length, end_height), color=sd.COLOR_YELLOW,
            width=1)
    sd.line(start_point=sd.get_point(beg_length - length_br / 2, end_height),
            end_point=sd.get_point(beg_length, end_height), color=sd.COLOR_YELLOW, width=1)
    sd.line(start_point=sd.get_point(end_length - length_br / 2, beg_height),
            end_point=sd.get_point(end_length, beg_height), color=sd.COLOR_YELLOW, width=1)
#bricks(300, 900, 50, 600, 50, 25)



# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

#sd.pause()
# зачет!