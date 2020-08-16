# -*- coding: utf-8 -*-

import os
import time
import shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class SortFile:
    output_path = 'C:\\Users\\asus\\PycharmProjects\\python_base1\\lesson_009\\icons'
    target_path = 'C:\\Users\\asus\\PycharmProjects\\python_base1\\lesson_009\\icons_by_year'

    def __init__(self, output_dir, target_dir):
        self.output_dir = output_dir
        self.target_dir = target_dir

    def __str__(self):
        return 'Файлы рассортированы по дате'

    def copy_file(self, output_path, target_path):
        for dirpath, dirnames, filenames in os.walk(output_path):
            print(dirpath, dirnames, filenames)
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                new_dir_path = os.path.join(str(target_path), str(file_time[0]), str(file_time[1]), str(file_time[2]))
                if (os.path.isdir(new_dir_path)) is False:
                    os.makedirs(new_dir_path)
                shutil.copyfile(full_file_path, os.path.join(new_dir_path, file))


file = SortFile('icons', 'icons_by_year')
file.copy_file(file.output_path, file.target_path)
print(file)
# зачет!
# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
