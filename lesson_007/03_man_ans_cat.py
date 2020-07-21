# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.cat = None
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            self.fullness += 10
            self.house.food -= 10
            cprint('{} поел'.format(self.name), color='yellow')
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        self.house.money += 150
        self.fullness -= 10
        cprint('{} сходил на работу'.format(self.name), color='blue')

    def watch_MTV(self):
        self.fullness -= 10
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')

    def shopping(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.food += 100
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):

        self.house = house
        self.fullness -= 10
        cprint('{} Въехал в дом'.format(self.name), color='cyan')

    def take_cat(self, cat, house):
        self.cat = cat
        self.cat.house = house
        cprint('{} взял в дом кота'.format(self.name), color='magenta')

    def buy_cat_food(self):
        self.house.cat_food += 50
        self.house.money -= 50
        cprint('{} купил котам еды'.format(self.name), color='magenta')

    def cleen_house(self):  # TODO typo error: cleen_house -> clean_house
        self.fullness -= 20
        self.house.dirt -= 100
        cprint('{} убрался в доме'.format(self.name), color='magenta')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.cat.fullness >= 0:
            # TODO внутри класса Человек не должно быть кошачьих активностей, кроме покупки человеком еды для кота
            if self.cat.fullness <= 30:
                self.cat.eat()
            elif dice == 1 or dice == 2 or dice == 3:  # TODO лучше использовать конструкцию dice in [...]
                self.cat.sleep()
            elif dice == 4 or dice == 5 or dice == 6:  # TODO аналогично, см. комментарий выше
                self.cat.tear_wallpaper()
        else:
            cprint('Кот умер', color='red')
            self.cat = None
        if self.fullness < 40:
            self.eat()
        elif self.house.food < 50:
            self.shopping()
        elif self.house.cat_food < 20:
            self.buy_cat_food()
        elif self.house.dirt > 100:
            self.cleen_house()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class Cat:

    def __init__(self, fullness, house):
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - кот, сытость {} '.format(
            self.fullness)

    def sleep(self):
        self.fullness -= 10
        cprint('Кот поспал', color='yellow')

    def eat(self):
        if self.house.cat_food >= 10:
            self.fullness += 20
            self.house.cat_food -= 10
            cprint('Кот поел', color='yellow')
        else:
            cprint('Кончилась кошачья еда', color='red')

    def tear_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint('Кот подрал обои', color='yellow')
        if self.house.dirt > 100:
            cprint('Дома грязь', color='red')


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 50
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кошачьей еды осталось {}, грязь {}'.format(
            self.food, self.money, self.cat_food, self.dirt)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

my_sweet_home = House()
cat = Cat(50, None)
for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)
    citizen.take_cat(cat, my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citizen in citizens:
        citizen.act()
        # TODO теперь получается, что каждый житель взял по коту, но сам кот участия в жизни дома не проявляет
        # TODO сейчас судя по исходному коду, кот живёт внутри своего хозяина. Это неверно!
        #  Здесь должен вызываться кошачий act(). Не привязывайте его к конкретному жителю дома. То есть вне цикла
    print('--- в конце дня ---')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
