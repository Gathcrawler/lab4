#!/usr/bin/env python3
from librip.gens import field
from librip.gens import gen_random


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1


print(list(gen_random(1,45, 16)))
print(list(field(goods, 'title')))

print(list(field(goods, 'title', 'price', 'color')))

