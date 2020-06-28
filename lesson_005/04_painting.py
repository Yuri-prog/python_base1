# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)
import simple_draw as sd
# TODO: модули в питоне принято именовать маленькими буквами
import Painting.fractal
import Painting.rainbow
import Painting.smile
import Painting.snowfall
import Painting.wall
import Painting.sun
sd.resolution = (1600, 800)

left_bottom = sd.get_point(0, 0)
right_top = sd.get_point(1600, 50)
sd.rectangle(left_bottom=left_bottom , right_top=right_top, color=sd.COLOR_BLACK, width=0)
sd.line(start_point=sd.get_point(300,  400), end_point=sd.get_point(975, 400), color=sd.COLOR_YELLOW, width=1)
sd.line(start_point=sd.get_point(300,  400), end_point=sd.get_point(635, 550), color=sd.COLOR_YELLOW, width=1)
sd.line(start_point=sd.get_point(635, 550), end_point=sd.get_point(975, 400), color=sd.COLOR_YELLOW, width=1)
Painting.wall.bricks(400, 900, 50, 400, 50, 25)
sd.rectangle(left_bottom=sd.get_point(540, 140), right_top=sd.get_point(740, 300), color=sd.COLOR_DARK_GREEN, width=0)
Painting.rainbow.rainbow(600, -100, radius=1100)
sun_center = sd.get_point(430, 650)
sd.circle(center_position=sun_center, radius=60, color=sd.COLOR_YELLOW, width=0)
for angle in range(0, 360, 30):
     v = sd.get_vector(start_point=sun_center, angle=angle, length=120, width=4)
     v.draw()



Painting.smile.smile(620, 150, sd.COLOR_RED)
Painting.fractal.draw_branches(start_point=sd.get_point(1300, 50), angle=90, length=120, delta=30)

Painting.snowfall.for_painting(20)


# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
sd.pause()

#Илья, добрый день! Как запустить процессы параллельно? При попытке сделать анимацию, пока идет один процесс,
#остальные не запускаются.
# TODO: это так не работает. Чтобы был эффект анимации картинки, нужно понемногу изменять каждый объект в цикле.
