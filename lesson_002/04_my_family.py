#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mother', 'father', 'sister', 'brother', 'grandfather', 'grandmother']
print(my_family)


# список списков приблизителного роста членов вашей семьи
my_family_height = [['mother', 160],['father', 155],['sister', 165],['brother', 180],['grandfather', 170],['grandmother', 150]]
print(my_family_height)

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('father')



# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
m=my_family_height [0][1]
f=my_family_height [1][1]
s=my_family_height [2][1]
b=my_family_height [3][1]
gf=my_family_height [4][1]
gm=my_family_height [5][1]
my_family_height=(m, f, s, b, gf, gm)
s=sum(my_family_height)
print('Общий рост моей семьи', s, 'см')