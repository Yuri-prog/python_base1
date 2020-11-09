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
from decimal import Decimal

from termcolor import cprint, colored


def game():
    with open('rpg.json', 'r') as read_file:
        loaded_json_file = json.load(read_file)

    remaining_time = '123456.0987654321'
    current_location = loaded_json_file
    current_experience = 0
    current_date = datetime.datetime.now()
    loc_list = []
    game_events = []

    def monster_fight():
        if len(monsters) == 1:
            cprint(f'Вы атаковали монстра {monsters[0]}', color='blue')
            del_monster = monsters[0]
        else:
            while True:
                attaked_monster = input(colored('Выберите номер монстра:', color='yellow'))
                if not attaked_monster.isdigit() or int(attaked_monster) < 1 or int(attaked_monster) > len(monsters):
                    cprint('Неверный ввод, попробуйте еще раз', color='yellow')
                    continue
                cprint(f'Вы атаковали монстра {monsters[(int(attaked_monster) - 1)]}', color='blue')
                del_monster = monsters[(int(attaked_monster) - 1)]
                break

        for key, value in current_location.items():
            for i in value:
                if i == del_monster:
                    value.remove(i)
                    break
        monsters.remove(del_monster)

    def enter_loc():
        nonlocal current_location
        if len(locations) == 1:
            current_location = loc_list[0]

        else:
            while True:
                choose_loc = input(colored('Выберите локацию', color='yellow'))
                if not choose_loc.isdigit() or int(choose_loc) < 1 or int(choose_loc) > len(locations):
                    cprint('Неверный ввод, попробуйте еще раз', color='yellow')
                    continue
                current_location = loc_list[int(choose_loc) - 1]
                break

    def write_csv():
        with open('dungeon.csv', 'a', newline='') as out_csv:
            writer = csv.writer(out_csv)
            writer.writerow(['Game starts'])
            writer.writerows(game_events)
            writer.writerow(['Game over'])
            writer.writerow([])

    def quit():
        quit = input(colored('Хотите начать заново? y/n', color='yellow'))
        if quit == 'y':
            game()
        else:
            raise KeyError('Выход')

    while True:
        loc_list = []
        actions = ['Атаковать монстра', 'Перейти в другую локацию', 'Сдаться и выйти из игры']
        monsters = []
        locations = []

        try:
            for cur_loc, value in current_location.items():
                cprint(f'Вы в локации {cur_loc}', color='grey')
                cprint(f'Ваш опыт {current_experience}. Остаток времени до наводнения {remaining_time} секунд',
                       color='grey')
                new_event = [cur_loc, current_experience, current_date]
                game_events.append(new_event)
                if str(remaining_time) < str(0):
                    cprint('Наводнение! Вы утонули', color='red')
                    write_csv()
                    quit()
                if cur_loc.startswith('Hatch'):
                    if current_experience >= 280:
                        cprint('Вы выиграли!!!', color='green')
                        write_csv()
                        quit()
                    else:
                        cprint('У Вас недостаточно опыта, чтобы открыть люк. Вы проиграли', color='red')
                        write_csv()
                        quit()
                current_list = current_location[cur_loc]
                for i in current_list:
                    if isinstance(i, dict):
                        loc_list.append(i)
                for i in value:
                    if isinstance(i, str):
                        if i.startswith('Mob') or i.startswith('Boss'):
                            monster = i
                            monsters.append(monster)
                        else:
                            continue
                    else:
                        for key1, value1 in i.items():
                            locations.append(key1)
                if len(monsters) == 1:
                    ending = ''
                elif 5 > len(monsters) > 1:
                    ending = 'а'
                else:
                    ending = 'ов'
                cprint(f'Перед Вами {len(monsters)} монстр{ending}', color='grey')
                for i, k in enumerate(monsters):
                    if k.startswith('Mob'):
                        monster_exp = k[7:9]
                        monster_time = k[12:]
                    elif k.startswith('Boss_'):
                        monster_exp = k[8:11]
                        monster_time = k[14:]
                    else:
                        monster_exp = k[11:14]
                        monster_time = k[17:]
                    cprint(
                        f'{i + 1}. {k}. Получаемый за битву опыт {monster_exp}, время на уничтожение {monster_time} секунд',
                        color='cyan')

                if len(locations) == 1:
                    ending = ''
                elif 5 > len(locations) > 1:
                    ending = 'а'
                else:
                    ending = 'ов'
                cprint(f'Перед Вами {len(locations)} вход{ending} в локации', color='grey')
                if len(locations) == 0:
                    cprint('Вы в тупике! Обратного хода нет. Вы проиграли', color='red')
                    write_csv()
                    quit()
                for i, k in enumerate(locations):
                    if k.startswith('Hatch'):
                        loc_time = k[8:]
                    else:
                        end = k.rfind('_', 7, 12)
                        loc_time = k[(end + 3):]
                    cprint(f'{i + 1}. {k}. Время достижения локации {loc_time} секунд', color='cyan')
            cprint('Выберите действие:', color='yellow')
            if len(monsters) == 0:
                actions.remove('Атаковать монстра')
            for i, k in enumerate(actions):
                cprint(f'{i + 1}. {k}', color='yellow')

            number = input()
            if not number.isdigit() or int(number) < 1 or int(number) > len(actions):
                print('Неверный ввод, попробуйте еще раз')
                continue
            if len(actions) == 3:
                if number == '1':
                    monster_fight()
                    current_experience += int(monster_exp)
                    remaining_time = Decimal(remaining_time) - Decimal(monster_time)
                elif number == '2':
                    enter_loc()
                    remaining_time = Decimal(remaining_time) - Decimal(loc_time)
                elif number == '3':
                    cprint('Вы сдаетесь.', color='red')
                    write_csv()

                    quit()
            elif len(actions) == 2:
                if number == '1':
                    enter_loc()
                    remaining_time = Decimal(remaining_time) - Decimal(loc_time)
                elif number == '2':
                    cprint('Вы сдаетесь.', color='red')
                    write_csv()
                    quit()

        except KeyError:
            break


game()
# Учитывая время и опыт, не забывайте о точности вычислений!
