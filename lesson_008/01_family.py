# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0


class Human:

    def __init(self, name, house):  # TODO здесь опечатка в названии метода
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        return 'Член семьи {}, сытость {}, счастье {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        self.fullness += 30
        self.house.food -= 30
        cprint(self.name, 'поел', color='green')  # TODO см. уже аналогичную проблему с cprint в gaming()


class Husband(Human):

    def __init__(self, name):  # TODO здесь ещё нужно принимать аргумент house
        super().__init__(name=name)  # TODO и здесь передавать house тоже
        self.name = name  # TODO эта строка не нужна
    # TODO И эта проблема уже другого порядка, не связанная с предыдущим вопросом

    def __str__(self):
        return super().__str__()

    def act(self):
        # TODO здесь аналогично, нужно вызывать сначала родительский act
        if 0 < self.fullness < 30:
            self.eat()
        elif self.fullness < 0:
            cprint(self.name, 'умер от голода', color='red')
            return
        elif self.happiness < 10:
            cprint(self.name, 'умер от депрессии', color='red')
            return
        elif self.house.money < 50:
            self.work()
        else:
            self.gaming()

    def work(self):
        self.house.money += 150
        self.fullness -= 10
        cprint(self.name, 'сходил на работу', color='green')

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        cprint(self.name + ' поиграл', color='green')  # TODO здесь self.name, 'поиграл' нужно объединить в одну строку
        # TODO иначе cprint не может корректно распарсить аргументы, которые этому методу переданы


class Wife(Human):

    def __init__(self, name):  # TODO требуется доработать по аналогии с методом __init__ в Husband
        super().__init__(name=name)
        self.name = name

    def __str__(self):
        return super().__str__()

    def act(self):
        # TODO вызывать act из родительского класса
        if 0 < self.fullness < 30:
            self.eat()
        elif self.fullness < 0:
            cprint(self.name, 'умерла от голода', color='red')
            return
        elif self.happiness < 10:
            cprint(self.name, 'умерла от депрессии', color='red')
            return
        elif self.house.money > 420:
            self.buy_fur_coat()
        elif self.house.dirt > 100:
            self.clean_house()

    def eat(self):
        self.fullness += 30
        self.house.food -= 30
        cprint(self.name, 'поела', color='green')

    def shopping(self):
        self.house.food += 70
        self.house.money -= 70
        self.fullness -= 10
        cprint(self.name, 'сходила в магазин за едой', color='green')

    def buy_fur_coat(self):
        self.house.money -= 350
        self.happiness += 60
        self.fullness -= 10
        cprint(self.name, 'купила шубу!!!', color='orange')

    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 10


home = House()
# TODO в двух строках ниже тоже требуются доработки
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.dirt += 5
    if home.dirt > 90:
        serge.happiness -= 10
        masha.happiness -= 10
    serge.act()
    masha.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')


# TODO после реализации первой части - отдать на проверку учителю
# TODO нужно всегда удалять все TODO по мере выполнения заданий
# TODO удалить неактуальные TODO

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
