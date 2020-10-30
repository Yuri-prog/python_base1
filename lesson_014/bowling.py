def get_score(game_result):
    tmp_results = []
    results = []
    strike_list = []
    sum = 0
    strike_sum = 0
    game_result = game_result.upper()
    for i in game_result:
        if i == 'X':
            frame_result = 20
            strike_sum += frame_result
            strike_list.append(i)
        else:
            tmp_results.append(i)
    if len(tmp_results) % 2 == 1:
        raise ValueError('Неверные данные. Ошибка в количестве данных.')
    for i in range(1, len(tmp_results), 2):
        results.append([tmp_results[i - 1], tmp_results[i]])
        if tmp_results[i] == '/':
            if tmp_results[i - 1].isdigit() is False and tmp_results[i - 1] != '-':
                raise ValueError('Неверные данные. Ошибка указателя spare.')
        if tmp_results[i] == '0':
            raise ValueError('Неверные данные.')
    for value in results:
        if value[0] == '-':
            value[0] = '0'
        if value[1] == '-':
            value[1] = '0'
        if value[0].isdigit() & value[1].isdigit():
            frame_result = int(value[0]) + int(value[1])
            if frame_result > 9:
                raise ValueError('Неверные данные. Сумма очков фрейма больше 9.')
        elif value[1] == '/':
            frame_result = 15
        else:
            raise ValueError('Неверные данные')
        sum += frame_result
    common_sum = strike_sum + sum
    if (len(strike_list) + len(results)) != 10:
        raise ValueError('Ошибка данных. Число фреймов не соответствует заданному.')
    #print(common_sum)
    return common_sum


# get_score('811/X--3/XX171/45')
# get_score('811/X--3/XX171/00')
# get_score('XXXXX//XXXX') # Здесь исправил.
# get_score('X-/XXXXXXXX')

def get_score_inter(game_result):
    tmp_results = []
    results = []
    strike_list = []
    sum = 0
    game_result = game_result.upper()
    for i in game_result:
        if i != 'X':
            tmp_results.append(i)

    if len(tmp_results) % 2 == 1:
        raise ValueError('Неверные данные. Ошибка в количестве данных.')
    for i in range(1, len(tmp_results), 2):
        results.append([tmp_results[i - 1], tmp_results[i]])
        if tmp_results[i] == '/':
            if tmp_results[i - 1].isdigit() is False and tmp_results[i - 1] != '-':
                raise ValueError('Неверные данные. Ошибка указателя spare.')
        if tmp_results[i] == '0':
            raise ValueError('Неверные данные.')

    for value in results:
        if value[0] == '-':
            value[0] = '0'
        if value[1] == '-':
            value[1] = '0'
        if value[0].isdigit() & value[1].isdigit():
            frame_result = int(value[0]) + int(value[1])
            if frame_result > 9:
                raise ValueError('Неверные данные. Сумма очков фрейма больше 9.')
        elif value[1] == '/':
            continue
        else:
            raise ValueError('Неверные данные')
        sum += frame_result
    game_result_list = []
    spare_result_sum = 0
    strike_result_sum = 0
    for i in game_result:
        if i == '-':
            i = '0'
        elif i == 'X':
            i = '10'
        game_result_list.append(i)
    for i, x in enumerate(game_result_list):
        if x == '/':
            game_result_list.remove(x)
            game_result_list.insert(i, str(10 - int(game_result_list[i - 1])))
            if i < (len(game_result_list)-1):
                if (game_result_list[i + 1]) != '10':
                    spare_result = 10 + int(game_result_list[i + 1])
                else:
                    spare_result = 20
            else:
                spare_result = 10
            spare_result_sum += spare_result
        elif x == '10':
            if i < (len(game_result_list) - 2):
                if game_result_list[i+2].isdigit():
                    strike_result = 10 + int(game_result_list[i + 1]) + int(game_result_list[i + 2])
                else:
                    strike_result = 20
            elif i == (len(game_result_list) - 2):
                strike_result = 20
            else:
                strike_result = 10
            strike_list.append(x)
            strike_result_sum += strike_result
    common_sum = strike_result_sum + spare_result_sum + sum
    if (len(strike_list) + len(results)) != 10:
        raise ValueError('Ошибка данных. Число фреймов не соответствует заданному.')
    #print(common_sum)
    return common_sum


#get_score('XXXXXXXXXX')
#get_score_inter('547/23Xx-3x81453-')
