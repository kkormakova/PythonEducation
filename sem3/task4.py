# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число для преобразования десятичного числа в двоичное: '))
temp = n
num = ''
while n != 0:
    num = str(n % 2) + num
    n //= 2
print(f'{temp} -> {num}')