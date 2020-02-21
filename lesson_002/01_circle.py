#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение площади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
radius = 42
pi = 3.1415926
s = pi * radius ** 2
print(round(s, 4))

# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у
# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
t = ((point_1[0] ** 2) + (point_1[1] ** 2)) ** 0.5
print(t >= radius)  # TODO По условию должно выводиться True, если точка лежит внутри круга (если t меньше радиуса)
# TODO У вас наоборот, надо использовать другой оператор сравнения

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
a = ((point_2[0] ** 2) + (point_2[1] ** 2)) ** 0.5
print(a >= radius)  # TODO И тут

# Пример вывода на консоль:
#
# 77777.7777
# False
# False
