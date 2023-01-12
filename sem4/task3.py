# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

listNum = list(map(int, input('Введите числа через пробел: ').split()))
print(f'Наш исходный список: {listNum}')
newList = []
[newList.append(i) for i in listNum if i not in newList]
print(f'Список из неповторяющихся элементов: {newList}')
