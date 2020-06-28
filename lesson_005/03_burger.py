# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger as mb
def double_cheezeburger():
    mb.bun()
    mb.cutlet()
    mb.cucumber()
    mb.tomato()
    mb.mayo()
    mb.cheeze()
    mb.cheeze()
    mb.cheeze()
    print(mb.my_burger)

#double_cheezeburger()

def super_burger():
    mb.bun()
    mb.cutlet()
    mb.onion()
    mb.jam()
    print(mb.my_burger)
super_burger()

# зачет!