# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(part1=self, part2=other, name='Шторм')
        elif isinstance(other, Fire):
            return Steam(part1=self, part2=other, name="Пар")
        elif isinstance(other, Ground):
            return Dirt(part1=self, part2=other, name='Грязь')
        elif isinstance(other, Airplane):
            return Hydroplane(part1=self, part2=other, name='Самолет')


class Air:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm(part1=self, part2=other, name='Шторм')
        elif isinstance(other, Fire):
            return Lightning(part1=self, part2=other, name='Молния')
        elif isinstance(other, Ground):
            return Dust(part1=self, part2=other, name='Пыль')
        if isinstance(other, Airplane):
            return Flight(part1=self, part2=other, name='Полет')


class Fire:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning(part1=self, part2=other, name='Молния')
        elif isinstance(other, Water):
            return Steam(part1=self, part2=other, name='Пар')
        elif isinstance(other, Ground):
            return Lava(part1=self, part2=other, name='Лава')
        elif isinstance(other, Airplane):
            return Big_fire(part1=self, part2=other, name='Пожар')


class Ground:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust(part1=self, part2=other, name='Пыль')
        elif isinstance(other, Water):
            return Dirt(part1=self, part2=other, name='Грязь')
        elif isinstance(other, Fire):
            return Lava(part1=self, part2=other, name='Лава')
        elif isinstance(other, Airplane):
            return Landing(part1=self, part2=other, name='Посадка')


class Storm:

    def __init__(self, part1, part2, name):
        self.part1 = part1
        self.part2 = part2
        self.name = name

    def __str__(self):
        return self.name


class Steam:

    def __init__(self, part1, part2, name):
        self.part1 = part1
        self.part2 = part2
        self.name = name

    def __str__(self):
        return self.name


class Dirt:

    def __init__(self, part1, part2, name):
        self.part1 = part1
        self.part2 = part2
        self.name = name

    def __str__(self):
        return self.name


class Lightning:

    def __init__(self, part1, part2, name):
        self.part1 = part1
        self.part2 = part2
        self.name = name

    def __str__(self):
        return self.name


class Dust:

    def __init__(self, part1, part2, name):
        self.part1 = part1
        self.part2 = part2
        self.name = name

    def __str__(self):
        return self.name


class Lava:

    def __init__(self, part1, part2, name):
        self.part1 = part1
        self.part2 = part2
        self.name = name

    def __str__(self):
        return self.name


print(Water('Вода'), '+', Air('Воздух'), '=', Water('Вода') + Air('Воздух'))
print(Water('Вода'), '+', Fire('Огонь'), '=', Water('Вода') + Fire('Огонь'))
print(Water('Вода'), '+', Ground('Земля'), '=', Water('Вода') + Ground('Земля'))
print(Air('Воздух'), '+', Fire('Огонь'), '=', Air('Воздух') + Fire('Огонь'))
print(Air('Воздух'), '+', Ground('Земля'), '=', Air('Воздух') + Ground('Земля'))
print(Fire('Огонь'), '+', Ground('Земля'), '=', Fire('Огонь') + Ground('Земля'))


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.


class Airplane:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            return Flight(part1=self, part2=other)
        elif isinstance(other, Water):
            return Hydroplane(part1=self, part2=other)
        elif isinstance(other, Ground):
            return Landing(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Big_fire(part1=self, part2=other)


class Flight:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Полет'


class Hydroplane:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Гидросамолет'


class Landing:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Посадка'


class Big_fire:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пожар'


print(Airplane('Самолет'), '+', Air('Воздух'), '=', Airplane('Самолет') + Air('Воздух'))
print(Airplane('Самолет'), '+', Ground('Земля'), '=', Airplane('Самолет') + Ground('Земля'))
print(Airplane('Самолет'), '+', Water('Вода'), '=', Airplane('Самолет') + Water('Вода'))
print(Airplane('Самолет'), '+', Fire('Огонь'), '=', Airplane('Самолет') + Fire('Огонь'))


