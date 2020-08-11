# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

file_name = 'voyna-i-mir.txt'


class Text:
    alphabet = list(range(0x0041, 0x005B)) + list(range(0x0061, 0x007B)) + list(range(0x0410, 0x0450))

    def __init__(self, file_name):
        self.file_name = file_name
        self.total_quant = []
        self.letter_quant = ()
        self.sum = 0

    def count_letters(self):
        with open(file_name, 'r', encoding='cp1251') as file:
            total = file.read()
            for letter in self.alphabet:
                self.letter_quant = (chr(letter), total.count(chr(letter)))
                self.total_quant.append(self.letter_quant)
                self.total_quant.sort(key=lambda i: i[1], reverse=True)

    def print_table(self):
        print('+{txt:-<6}+{txt:-<10}+'.format(txt=''))
        print('|{txt1:^6}|{txt2:^10}|'.format(txt1='Буква', txt2='Частота'))
        print('+{txt:-<6}+{txt:-<10}+'.format(txt=''))
        for self.letter_quant in self.total_quant:
            print('|{txt1:^6}|{txt2:^10}|'.format(txt1=self.letter_quant[0], txt2=self.letter_quant[1]))
            self.sum += self.letter_quant[1]
        print('+{txt:-<6}+{txt:-<10}+'.format(txt=''))
        print('|{txt1:^6}|{txt2:^10}|'.format(txt1='Итого', txt2=self.sum))
        print('+{txt:-<6}+{txt:-<10}+'.format(txt=''))


file = Text('voyna-i-mir.txt')
file.count_letters()
file.print_table()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
