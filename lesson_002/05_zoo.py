#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
zoo.insert(1, 'bear')
#  и выведите список на консоль
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print(zoo)

# уберите слона
zoo.remove('elephant')
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
lion = ('Лев сидит в клетке №', zoo.index('lion') + 1)
lark = ('Жаворонок сидит в клетке №', zoo.index('lark') + 1)
print(lion)
print(lark)

#зачет!