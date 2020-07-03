import random

computer_number = []
digit_list = []
your_number = []
differ_list = []

def comp_number():
    global computer_number
    for i in range(0, 10):
        digit_list.append(i)
    dig_list = random.sample(digit_list, len(digit_list))  # случайный список от 0 до 9
    for i in range(4):
            x = dig_list[i]
            computer_number.append(x)
    if computer_number[0] == 0:
        computer_number.remove(0) #удаление нуля с первой позиции
        for i in range(1, 3):
            y = random.randint(1, 3)
        computer_number.insert(y, 0) #подстановка удаленного нуля в случайное место



def take_number(your_number_string):
    global your_number
    if your_number_string.isdigit() == True:
        your_number = [int(x) for x in list(your_number_string)]
    else:
        return False
    if len(your_number) != len(set(your_number)):
        return False
    elif your_number[0] == 0:
        return False
    elif len(your_number) != 4:
        return False
    elif your_number_string.isdigit() == False:
        return False
    return your_number


def check_match():
    differ_list = []
    cow_words =  {0:'коров', 1:'корова', 2:'коровы', 3:'коровы', 4:'коровы'}
    bull_words = {0:'быков', 1:'бык', 2:'быка', 3:'быка', 4:'быка'}
    for i in range(4):
        differ_list.append(computer_number[i]-your_number[i])

    check_bull = differ_list.count(0)
    if check_bull :
         print(check_bull, bull_words[check_bull])
         if check_bull == 4:
             return check_bull
    else:
         print(0, bull_words[0])
    sum_number = computer_number + your_number
    check_cow_set = set(sum_number)
    check_cow = 8 - check_bull - len(check_cow_set)
    print(check_cow, cow_words[check_cow])

#check_match()