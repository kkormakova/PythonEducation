# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random


def writeFile(num):
    with open('file.txt', 'w') as data:
        for i in range(num):
            data.write(f'{random.randint(0, 2*num)}\n')


def readFile():
    with open('file.txt', 'r') as data:
        indexes = list(map(int, data.readlines()))
    return indexes


n = int(input('Введите число N: '))
listNumbers = []
for i in range(-n, n+1):
    listNumbers.append(i)
print(f'Полученный список чисел в промежутке [{-n};{n}]: {listNumbers}')
writeFile(n)
listIndex = readFile()
operation = 1
for i in range(len(listIndex)):
    operation *= listNumbers[listIndex[i]]
print(
    f'Произведение элементов с позиций указанных в файле file.txt равно = {operation}')
