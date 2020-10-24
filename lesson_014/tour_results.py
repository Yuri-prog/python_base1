from bowling import get_score

text_file = 'tournament.txt'
write_file = 'tournament_result.txt'


def tour_results(text_file):
    text_dict = {}
    new_list = []
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
                    try:
                        score = get_score(result)
                        if score > score1:
                            max = tour_player_list[0]
                            score1 = score
                        tour_player_list = ['{:<10}'.format(tour_player_list[0]), '{:<20}'.format(result),
                                            '{:<10}'.format(score)]
                        tour_player = '\t'.join(tour_player_list)
                    except ValueError as exc:
                        tour_player_list = ['{:<10}'.format(tour_player_list[0]), '{:<25}'.format(result),
                                            '{:>10}'.format(str(exc))]
                        tour_player = '\t'.join(tour_player_list)
                else:
                    if max:
                        tour_player = f'\nПобедитель {max}!'
                    else:
                        tour_player = '\nВ туре нет победителя из-за ошибочных данных'

                new_list.append(tour_player)
        new_results = '\n'.join(new_list)
        #print(new_results)
        return new_results


def write_result(text_file, write_file):
    tour_results(text_file)
    with open(write_file, mode='w', encoding='utf8') as file:
        file.write(tour_results(text_file))

# write_result(text_file, write_file)
