# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def operation(e):
    if e == 1:
        return 1
    else:
        return e * operation(e-1)


num = int(input('Введите число N: '))
list = []
for i in range(1, num+1):
    list.append(operation(i))
print(f'Произведение чисел от 1 до {num} = {list}')
