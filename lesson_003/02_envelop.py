# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта,
# если размеры равны - лист входит в конверт впритирку)
# Не забывайте, что лист бумаги можно перевернуть и попробовать вставить в конверт другой стороной.
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

def push_paper(paper_x, paper_y):
    envelop_x = 10
    envelop_y = 7
    if envelop_x >= paper_x and envelop_y >= paper_y:
        print('ДА')
    elif envelop_x >= paper_y and envelop_y >= paper_x:
        print('ДА')
    else:
        print('НЕТ')

push_paper(11, 9)

# зачет!

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

# hole_x, hole_y = 8, 9

x = brick_x, brick_y, brick_z = 11, 10, 2


list_1 = brick_x, brick_y, brick_z = 11, 2, 10
list_2 = brick_x, brick_y, brick_z = 10, 11, 2
list_3 = brick_x, brick_y, brick_z = 10, 2, 11
list_4 = brick_x, brick_y, brick_z = 2, 10, 11
list_5 = brick_x, brick_y, brick_z = 2, 11, 10
list_6 = brick_x, brick_y, brick_z = 3, 5, 6
list_7 = brick_x, brick_y, brick_z = 3, 6, 5
list_8 = brick_x, brick_y, brick_z = 6, 3, 5
list_9 = brick_x, brick_y, brick_z = 6, 5, 3
list_10 = brick_x, brick_y, brick_z = 5, 6, 3
list_11 = brick_x, brick_y, brick_z = 5, 3, 6
list_12 = brick_x, brick_y, brick_z = 11, 3, 6
list_13 = brick_x, brick_y, brick_z = 11, 6, 3
list_14 = brick_x, brick_y, brick_z = 6, 11, 3
list_15 = brick_x, brick_y, brick_z = 6, 3, 11
list_16 = brick_x, brick_y, brick_z = 3, 6, 11
list_17 = brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)
big_list = [list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_8, list_10, list_11, list_12, list_13, list_14, list_15, list_16, list_17, ]

def push_brick(brick_x, brick_y, brick_z):
    list_hole = hole_x, hole_y = 8, 9
    new_list = []
    for x in big_list:
        x = sorted(x)  #если хотя бы 2 стороны крпича проходят в отверстие, пройдет и весь кирпич. Поэтому сторону
        del x[2]               # с максимальной длиной отбрасываем.
        new_list.append(x)
    for k, i in enumerate(new_list, 1):
    #for i in new_list:
        if (list_hole[0] >= i[0] and list_hole[1] >= i[1]) or (list_hole[0] >= i[1] and list_hole[1] >= i[0]):
            print('Кирпич №', k, 'проходит в отверстие',)
        else:
            print('Кирпич №', k, 'не проходит в отверстие',)


push_brick(brick_x, brick_y, brick_z)