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

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Steam(part1=self, part2=other)
        elif isinstance(other, Ground):
            return Dirt(part1=self, part2=other)
        elif isinstance(other, Airplane):
            return Hydroplane(part1=self, part2=other)

class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Lightning(part1=self, part2=other)
        elif isinstance(other, Ground):
            return Dust(part1=self, part2=other)
        if isinstance(other, Airplane):
            return Flight(part1=self, part2=other)

class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning(part1=self, part2=other)
        elif isinstance(other, Water):
            return Steam(part1=self, part2=other)
        elif isinstance(other, Ground):
            return Lava(part1=self, part2=other)
        elif isinstance(other, Airplane):
            return Big_fire(part1=self, part2=other)


class Ground:

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust(part1=self, part2=other)
        elif isinstance(other, Water):
            return Dirt(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Lava(part1=self, part2=other)
        elif isinstance(other, Airplane):
            return Landing(part1=self, part2=other)

class Storm:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Шторм'


class Steam:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пар'


class Dirt:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Грязь'


class Lightning:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Молния'


class Dust:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пыль'


class Lava:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Лава'


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Ground(), '=', Water() + Ground())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Ground(), '=', Air() + Ground())
print(Fire(), '+', Ground(), '=', Fire() + Ground())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.


class Airplane:

    def __str__(self):
        return 'Самолет'

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

print(Airplane(), '+', Air(), '=', Airplane() + Air())
print(Airplane(), '+', Ground(), '=', Airplane() + Ground())
print(Airplane(), '+', Water(), '=', Airplane() + Water())
print(Airplane(), '+', Fire(), '=', Airplane() + Fire())