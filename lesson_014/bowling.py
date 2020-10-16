

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
    if len(tmp_results)%2 == 1:
        raise ValueError('Неверные данные. Ошибка в количестве данных.')
    for i in range(1, len(tmp_results), 2):
        results.append([tmp_results[i-1], tmp_results[i]])
        if tmp_results[i] == '/':
            if tmp_results[i-1].isdigit() is False and tmp_results[i-1] != '-':
                raise ValueError('Неверные данные. Ошибка указателя spare.')
    for value in results:
        if value[0] == '-':
            value[0] = '0'
        if value[1] == '-':
            value[1] = '0'
        if value[0].isdigit()&value[1].isdigit():
            frame_result = int(value[0])+int(value[1])
            if frame_result > 10:
                raise ValueError('Неверные данные. Сумма очков фрема больше 10.')
        elif value[1] == '/':
            frame_result = 15
        else:
            raise ValueError('Неверные данные')
        sum += frame_result
    common_sum = strike_sum + sum
    if (len(strike_list)+len(results)) != 10:
        raise ValueError('Ошибка данных. Число фреймов не соответствует заданному.')
    print(common_sum)
    return common_sum

#get_score('XXXXX47XXXX')
#get_score('XXXXX//XXXX') # Здесь исправил.
#get_score('X-/XXXXXXXX')
