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
zoopark=zoo+birds
#  и выведите список на консоль
print(zoopark)


# уберите слона
del zoopark[3]
#  и выведите список на консоль
print(zoopark)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
lion=('Лев сидит в клетке №', zoopark.index('lion')+1)
lark=('Жаворонок сидит в клетке №', zoopark.index('lark')+1)
print(lion)
print(lark)




