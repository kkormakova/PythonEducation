# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите число n: '))
listSimple = []
temp = num
simple = 2
while num > 1:
    if num % simple == 0:
        listSimple.append(simple)
        num = num/simple
    else:
        simple += 1
print(f'Простые множители числа {temp}: {listSimple}')
