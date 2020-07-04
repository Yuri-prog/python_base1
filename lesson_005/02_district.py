# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
from shlex import join



import district.central_street.house1.room1 as ch1r1
import district.central_street.house1.room2 as ch1r2
import district.central_street.house2.room1 as ch2r1
import district.central_street.house2.room2 as ch2r2
import district.soviet_street.house1.room1 as sh1r1
import district.soviet_street.house1.room2 as sh1r2
import district.soviet_street.house2.room1 as sh2r1
import district.soviet_street.house2.room2 as sh2r2



district = ch1r1.folks + ch1r2.folks + ch2r1.folks + ch2r2.folks + sh1r1.folks + sh1r2.folks + sh2r1.folks + sh2r2.folks
print('На районе живут', ', '.join(district), '.')



# зачет!
