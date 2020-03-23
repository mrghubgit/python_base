# -*- coding: utf-8 -*-
import random
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

# TODO Нужно подправить стиль кода - используйте Code/Refromat Code
# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point, step, color_bubble):
    radius_bubble = 50
    for _ in range(3):
        radius_bubble += step
        sd.circle(center_position=point, radius=radius_bubble, width=2, color=color_bubble)


bubble(point=sd.get_point(300, 300), step=5, color_bubble=sd.random_color())

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point_bubble = sd.get_point(x, 100)
    bubble(point=point_bubble, step=15, color_bubble=sd.COLOR_RED)

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point_bubble = sd.get_point(x, y)
        bubble(point=point_bubble, step=5, color_bubble=sd.COLOR_WHITE)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point_bubble = sd.random_point()
    step = random
    bubble(point=point_bubble, step= 10, color_bubble=sd.random_color())

sd.pause()


