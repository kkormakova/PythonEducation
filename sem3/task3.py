# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
numList = []
for i in range(7):
    numList.append(round(random.uniform(0.1, 10), 3))
print(f'Наш список вещественных чисел: {numList}')
newList = []
for i in range(7):
    newList.append(round(numList[i] % 1, 3))
max = newList[0]
min = newList[0]
for i in range(1, 7):
    if max < newList[i]:
        max = newList[i]
    elif min > newList[i]:
        min = newList[i]
print(
    f'Максимальное значение дробной части = {max}\nМинимальное значение дробной части = {min}\nИх разница = {round(max-min, 3)}')
