# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число для составления списка чисел Фибоначчи: '))
fibList = [0, 1]
for i in range(n-1):
    fibList.append(fibList[i]-fibList[i+1])
fibList.reverse()
fibList.append(1)
for j in range(len(fibList)-2, len(fibList)-2+n-1):
    fibList.append(fibList[j]+fibList[j+1])
print(fibList)
