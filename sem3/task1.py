# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
list = []
for i in range(random.randint(3, random.randint(6, 30))):
    list.append(random.randint(1, 100))
print(f'Наш полученный список чисел: {list}')
sum = 0
for i in range(1, len(list)):
    if i % 2 != 0:
        sum += list[i]
print(f'Сумма чисел на нечетных позициях равна {sum}')
