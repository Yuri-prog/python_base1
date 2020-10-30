from bowling import get_score, get_score_inter

text_file = 'tournament.txt'
write_file = 'tournament_result.txt'
version = 'inter'

def tour_results(text_file, version):
    text_dict = {}
    new_list = []
    players_list = []
    players = {}
    sum_max = []
    with open(text_file, mode='r', encoding='utf8') as file:
        for line in file:
            text_file += line
            text_list = text_file.split('\n\n')
        for i in text_list:
            j = str(i).split('\n')
            n = {j[0]: j[1:]}
            text_dict.update(n)
        for key, value in text_dict.items():
            score1 = 0
            max = None
            if len(key) > 10:
                key_1 = key[17:]
            else:
                key_1 = key[3:]
            new_list.append('{:*^90} \n'.format(key_1 + ' '))
            for tour_player in value:
                if not tour_player.startswith('winner'):
                    tour_player_list = tour_player.split('\t')
                    result = tour_player_list[1]
                    players_list.append(tour_player_list[0])
                    if version != 'russian' and version != 'inter':
                        raise ValueError('Ошибка. Не указана версия программы расчета.')
                    else:
                        try:
                            if version == 'russian':
                                score = get_score(result)
                            elif version == 'inter':
                                score = get_score_inter(result)
                            if score > score1:
                                max = tour_player_list[0]
                                score1 = score
                            tour_player_list1 = ['{:<10}'.format(tour_player_list[0]), '{:<20}'.format(result),
                                                 '{:<10}'.format(score)]
                            tour_player1 = '\t'.join(tour_player_list1)
                        except ValueError as exc:
                            tour_player_list1 = ['{:<10}'.format(tour_player_list[0]), '{:<25}'.format(result),
                                                 '{:>10}'.format(str(exc))]
                            tour_player1 = '\t'.join(tour_player_list1)
                else:
                    if max:
                        sum_max.append(max)
                        tour_player1 = f'\nПобедитель {max}!'
                    else:
                        tour_player1 = '\nВ туре нет победителя из-за ошибочных данных'

                y = {tour_player_list[0]: [players_list.count(tour_player_list[0]),
                                           sum_max.count(tour_player_list[0])]}  # Выполнение дополнительного задания
                players.update(y)
                sorted_list = sorted(players.items(), key=lambda x: (x[1][1], x[1][0]), reverse=True)
                new_list.append(tour_player1)
        print('+', 8 * '-', '+', 10 * '-', '+', 12 * '-', '+', 11 * '-', '+')
        print('|{:^10}|'.format('Место'), '{:^10}'.format('Игрок'), '|{:<14}|'.format('Сыграно матчей'),
              '{:<12}|'.format('Всего побед'))
        print('+', 8 * '-', '+', 10 * '-', '+', 12 * '-', '+', 11 * '-', '+')
        k = 1
        for i in sorted_list:
            print('|{:^10}|'.format(k), '{:^10}'.format(i[0]), '|{:^14}|'.format(i[1][0]), '{:^12}|'.format(i[1][1]))
            k += 1
        print('+', 8 * '-', '+', 10 * '-', '+', 12 * '-', '+', 11 * '-', '+')
        new_results = '\n'.join(new_list)

    return new_results


def write_result(text_file, write_file, version):
    with open(write_file, mode='w', encoding='utf8') as file:
        file.write(tour_results(text_file, version))


#write_result(text_file, write_file, version)


