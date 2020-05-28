# -*- coding: utf-8 -*-

# Нужно собрать информацию об операционной системе и версии пайтона



import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture())
print(info)

with open('os_info.txt', 'w', encoding='utf8') as ff:
    ff.write(info)


#Добрый день! У меня программа не работает. Выдает Process finished with exit code 0.
# Сначала ругался, что нет интерпретатора, потом я указал путь к интерпретатору Python 3.8, получил такой результат.
#Git Bash при попытке установить pip install ipython пишет, что команда pip не найдена.


#Переустановил Питон, все проблемы решены. Спасибо.