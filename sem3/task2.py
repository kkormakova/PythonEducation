# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
listNum = []
for i in range(random.randint(3, 10)):
    listNum.append(random.randint(1, 100))
print(f'Наш список чисел: {listNum}')
listOper = []
if len(listNum) % 2 != 0:
    lengthOper = len(listNum)//2+1
else:
    lengthOper = len(listNum)//2
for i in range(lengthOper):
    temp = listNum[i]*listNum[len(listNum)-i-1]
    listOper.append(temp)
print(f'Произведение пар чисел равно {listOper}')
