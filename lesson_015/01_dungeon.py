# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...

import csv
import datetime
import json
import re
from decimal import Decimal

from termcolor import cprint, colored

remaining_time = '123456.0987654321'
json_file = 'rpg.json'
csv_file = 'dungeon.csv'


class Readwrite:
    def __init__(self, json_file, csv_file):
        self.json_file = json_file
        self.csv_file = csv_file
        self.loaded_json_file = {}
        self.game_events = []

    def open_json(self):
        with open(self.json_file, 'r') as read_file:
            self.loaded_json_file = json.load(read_file)
            return self.loaded_json_file

    def write_csv(self):
        with open('dungeon.csv', 'a', newline='') as out_csv:
            writer = csv.writer(out_csv)
            writer.writerow(['Game starts'])
            writer.writerows(self.game_events)
            writer.writerow(['Game over'])
            writer.writerow([])

    def quit(self):
        quit = input(colored('Хотите начать заново? y/n', color='yellow'))
        if quit == 'y':
            gameplay.current_experience = 0
            gameplay.remaining_time = remaining_time
            caves.current_location = readwrite.open_json()
            gameplay.game()
        else:
            raise KeyError('Выход')


class Caves:
    def __init__(self):
        self.current_location = readwrite.open_json()
        self.locations = []
        self.loc_list = []
        self.choose_loc = ''
        self.loc_time_list = []

    def enter_loc(self):
        if len(self.locations) == 1:
            self.choose_loc = '1'
            self.current_location = self.loc_list[0]

        else:
            while True:
                self.choose_loc = input(colored('Выберите локацию', color='yellow'))
                if not self.choose_loc.isdigit() or int(self.choose_loc) < 1 or int(self.choose_loc) > len(
                        self.locations):
                    cprint('Неверный ввод, попробуйте еще раз', color='yellow')
                    continue
                self.current_location = self.loc_list[int(self.choose_loc) - 1]
                break

    def count_loc(self):
        if len(self.locations) == 1:
            ending = ''
        elif 5 > len(self.locations) > 1:
            ending = 'а'
        else:
            ending = 'ов'
        cprint(f'Перед Вами {len(self.locations)} вход{ending} в локации', color='grey')
        if len(self.locations) == 0:
            cprint('Вы в тупике! Обратного хода нет. Вы проиграли', color='red')
            readwrite.write_csv()
            readwrite.quit()
        loc_time_pattern = r'\w+_tm(\d{0,3}.{0,1}\d+)'
        self.loc_time_list = re.findall(loc_time_pattern, str(self.locations))
        loc_and_time = list(zip(range(len(self.locations)), self.locations, self.loc_time_list))
        for num in loc_and_time:
            number_loc = num[0]
            loc = num[1]
            loc_time = num[2]
            cprint(f'{number_loc + 1}. {loc}. Время достижения локации {loc_time} секунд', color='cyan')


class Monsters:
    def __init__(self):
        self.monsters = []
        self.monster_exp = ''
        self.monster_time = ''

    def monster_fight(self):
        if len(self.monsters) == 1:
            cprint(f'Вы атаковали монстра {self.monsters[0]}', color='blue')
            del_monster = self.monsters[0]
        else:
            while True:
                attaked_monster = input(colored('Выберите номер монстра:', color='yellow'))
                if not attaked_monster.isdigit() or int(attaked_monster) < 1 or int(attaked_monster) > len(
                        self.monsters):
                    cprint('Неверный ввод, попробуйте еще раз', color='yellow')
                    continue
                cprint(f'Вы атаковали монстра {self.monsters[(int(attaked_monster) - 1)]}', color='blue')
                del_monster = self.monsters[(int(attaked_monster) - 1)]
                break

        for key, value in caves.current_location.items():
            for i in value:
                if i == del_monster:
                    value.remove(i)
                    break
        self.monsters.remove(del_monster)

    def count_monsters(self):
        if len(self.monsters) == 1:
            ending = ''
        elif 5 > len(self.monsters) > 1:
            ending = 'а'
        else:
            ending = 'ов'
        cprint(f'Перед Вами {len(self.monsters)} монстр{ending}', color='grey')
        monster_exp_pattern = r'\w+\d{0,3}_exp(\d{2,3})_tm\d{1,8}'
        monster_time_pattern = r'\w+\d{0,3}_exp\d{2,3}_tm(\d{1,8})'
        expm = re.findall(monster_exp_pattern, str(self.monsters))
        expt = re.findall(monster_time_pattern, str(self.monsters))
        monster_list = list(zip(range(len(self.monsters)), self.monsters, expm, expt))
        for num in monster_list:
            if self.monsters:
                number_monster = num[0]
                monster = num[1]
                self.monster_exp = num[2]
                self.monster_time = num[3]
                cprint(
                    f'{number_monster + 1}. {monster}. Получаемый за битву опыт {self.monster_exp},'
                    f'время на уничтожение {self.monster_time} секунд',
                    color='cyan')


class Gameplay:

    def __init__(self, remaining_time):
        self.actions = ['Атаковать монстра', 'Перейти в другую локацию', 'Сдаться и выйти из игры']
        self.remaining_time = remaining_time
        self.current_experience = 0
        self.current_date = datetime.datetime.now()

    def start(self):
        for cur_loc, value in caves.current_location.items():
            cprint(f'Вы в локации {cur_loc}', color='grey')
            cprint(
                f'Ваш опыт {gameplay.current_experience}. Остаток времени до наводнения {gameplay.remaining_time} секунд',
                color='grey')
            new_event = [cur_loc, gameplay.current_experience, self.current_date]
            readwrite.game_events.append(new_event)
            if Decimal(gameplay.remaining_time) < 0 or cur_loc.startswith('Hatch'):
                if Decimal(gameplay.remaining_time) < 0:
                    cprint('Наводнение! Вы утонули', color='red')
                elif cur_loc.startswith('Hatch'):
                    if gameplay.current_experience >= 280:
                        cprint('Вы выиграли!!!', color='green')
                    else:
                        cprint('У Вас недостаточно опыта, чтобы открыть люк. Вы проиграли', color='red')
                readwrite.write_csv()
                readwrite.quit()
            monster_pattern = r'\w+\d{0,3}_exp\d{2,3}_tm\d{1,8}'
            all_monsters = re.findall(monster_pattern, str(value))
            for name in value:
                if all_monsters and name == all_monsters[0]:
                    mons.monsters.append(all_monsters[0])
                    all_monsters.remove(all_monsters[0])
                else:
                    for key1, value1 in name.items():
                        caves.loc_list.append(name)
                        caves.locations.append(key1)

    def choose_action(self):

        cprint('Выберите действие:', color='yellow')
        if len(mons.monsters) == 0:
            if len(gameplay.actions) == 3:
                self.actions.remove('Атаковать монстра')
        for num, action in enumerate(self.actions):
            cprint(f'{num + 1}. {action}', color='yellow')
        number = input()
        if not number.isdigit() or int(number) < 1 or int(number) > len(self.actions):
            print('Неверный ввод, попробуйте еще раз')
            self.choose_action()
        if len(self.actions) == 3 and number == '1':
            mons.monster_fight()
            self.current_experience += int(mons.monster_exp)
            self.remaining_time = Decimal(self.remaining_time) - Decimal(mons.monster_time)
        elif (len(self.actions) == 3 and number == '2') | (len(self.actions) == 2 and number == '1'):
            caves.enter_loc()
            self.remaining_time = Decimal(self.remaining_time) - Decimal(
                caves.loc_time_list[(int(caves.choose_loc) - 1)])
        elif (len(self.actions) == 3 and number == '3') | (len(self.actions) == 2 and number == '2'):
            cprint('Вы сдаетесь.', color='red')
            readwrite.write_csv()
            readwrite.quit()

    def game(self):
        while True:
            caves.loc_list = []
            mons.monsters = []
            caves.locations = []
            readwrite.open_json()
            gameplay.actions = ['Атаковать монстра', 'Перейти в другую локацию', 'Сдаться и выйти из игры']

            try:
                gameplay.start()
                mons.count_monsters()
                caves.count_loc()
                gameplay.choose_action()

            except KeyError:
                break


if __name__ == '__main__':
    readwrite = Readwrite(json_file, csv_file)
    caves = Caves()
    mons = Monsters()
    gameplay = Gameplay(remaining_time)
    gameplay.game()
#зачёт!