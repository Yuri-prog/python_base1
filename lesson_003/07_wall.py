# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for x in range(0, 601, 100):
    for y in range(0, 600, 50):
       if y%100 == 0:  # TODO: пробелы вокруг %
        sd.rectangle(sd.get_point(x-50 , y), sd.get_point(x + 50, y + 50), color=sd.COLOR_YELLOW, width=1)  # TODO: отступы + пробел перед запятой
       else:
           sd.rectangle(sd.get_point(x, y), sd.get_point(x + 100, y + 50), color=sd.COLOR_YELLOW, width=1)





# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()
