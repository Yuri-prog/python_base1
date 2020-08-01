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
        self.cat_food = 30

    def __str__(self):
        return 'Дом, денег в тумбочке {}, еды {}, , кошачьей еды {}, грязь {}'.format(self.money, self.food,
                                                                                      self.cat_food, self.dirt)


class Human:

    def __init__(self, house, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        return 'Член семьи {}, сытость {}, счастье {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        self.fullness += 30
        self.house.food -= 30
        cprint(self.name + ' ест', color='green')

    def pet_cat(self):
        self.happiness += 5
        cprint(self.name + ' гладит кота', color='green')

    def act(self):
        if 0 <= self.fullness < 40:
            self.eat()
        elif self.fullness < 0:
            cprint(self.name + ', смерть от голода', color='red')
        elif self.happiness < 10:
            cprint(self.name + ', смерть от депрессии', color='red')


class Husband(Human):

    def __init__(self, house, name):
        super().__init__(house, name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        dice = randint(1, 3)
        if dice == 1:
            self.work()
        elif dice == 2:
            super().pet_cat()
        else:
            self.gaming()

    def work(self):
        self.house.money += 150
        self.fullness -= 10
        cprint(self.name + ' сходил на работу', color='blue')

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        cprint(self.name + ' поиграл', color='green')


class Wife(Human):

    def __init__(self, house, name):
        super().__init__(house, name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        if self.house.money > 500:
            self.buy_fur_coat()
        elif self.house.dirt > 110:
            self.clean_house()
        elif self.house.food < 80:
            self.shopping()
        elif self.house.cat_food < 20:
            self.buy_cat_food()
        else:
            super().pet_cat()

    def shopping(self):
        self.house.food += 70
        self.house.money -= 70
        self.fullness -= 10
        cprint(self.name + ' сходила в магазин за едой', color='blue')

    def buy_fur_coat(self):
        self.house.money -= 350
        self.happiness += 60
        self.fullness -= 10
        cprint(self.name + ' купила шубу!!!', color='green')

    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 10
        cprint(self.name + ' сделала уборку', color='blue')

    def buy_cat_food(self):
        self.house.money -= 50
        self.house.cat_food += 50
        cprint(self.name + ' купила коту еды', color='blue')


class Cat:

    def __init__(self, house, name):
        self.name = name
        self.house = house
        self.fullness = 30

    def __str__(self):
        return 'Кот {}, сытость {}'.format(self.name, self.fullness)

    def act(self):
        dice = randint(1, 2)
        if self.fullness < 10:
            self.eat()
        elif self.fullness < 0:
            cprint(self.name + ' сдох', color='red')
            return
        elif dice == 1:
            self.sleep()
        else:
            self.soil()

    def eat(self):
        self.house.cat_food -= 10
        self.fullness += 20
        cprint(self.name + ' поел', color='green')

    def sleep(self):
        self.fullness -= 10
        cprint(self.name + ' поспал', color='green')

    def soil(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint(self.name + ' подрал обои', color='green')


class Child(Human):

    def __init__(self, house, name):
        super().__init__(house, name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        self.sleep()

    def eat(self):
        self.fullness += 10
        self.house.food -= 10
        cprint(self.name + ' ест', color='green')

    def sleep(self):
        self.fullness -= 5
        cprint(self.name + ' поспал', color='green')


home = House()
serge = Husband(home, name='Сережа')
masha = Wife(home, name='Маша')
cat = Cat(home, name='Мурзик')
kolya = Child(home, name='сын Коля')

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    home.dirt += 5
    if home.dirt > 90:
        serge.happiness -= 10
        masha.happiness -= 10
    serge.act()
    masha.act()
    kolya.act()
    cat.act()

    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(home, color='cyan')


# зачёт первой части

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



######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(home, name='Сережа')
# masha = Wife(home, name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

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
