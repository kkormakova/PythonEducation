# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
listNum = [randint(1, 100) for i in range(10)]
print(f'Наш список: {listNum}')
print(
    f'Сумма элементов на нечетных позициях = {sum(x for i, x in enumerate(listNum) if i % 2 != 0)}')
