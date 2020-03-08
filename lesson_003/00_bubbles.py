# -*- coding: utf-8 -*-
from random import choice

import simple_draw as sd
from simple_draw import Point

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(300, 300)
radius_bubble = 50
for _ in range(3):
    radius_bubble += 5
    sd.circle(center_position=point, radius=radius_bubble, width=2)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point, step, color_bubble):
    radius_bubble = 50
    for _ in range(3):
        radius_bubble += step
        sd.circle(center_position=point, radius=radius_bubble, width=2, color=color_bubble)


bubble(point=sd.get_point(300, 300), radius_bubble=50, color_bubble=sd.random_color())
#TODO Вот здесь даёт ошибку, получается что, мы указываем точку то есть point, после указываем
#TODO радиус то есть radius_bubble, и цвет который будет выдаваться рандомно?


# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


