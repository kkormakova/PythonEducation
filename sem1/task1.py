print('Введите число, обозначающее день недели')
a = int(input())
if a == 0:
    print('Введите число от 1 до 7')
elif a > 7:
    print('Введите другое число')
elif a >= 1 and a <= 5:
    print('Это будний день!')
elif a >= 6 and a <= 7:
    print('Это выходной день!')
