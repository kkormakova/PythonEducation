# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def inputCords(x):
    xy = ['X', 'Y']
    cords = []
    for i in range(x):
        cords.append(int(input(f'Введите координату по оси {xy[i]}: ')))
    return cords


print('Введите координаты точки A')
pointA = inputCords(2)
print('Введите координаты точки B')
pointB = inputCords(2)
result = ((pointB[0]-pointA[0])**2 + (pointB[1]-pointA[1])**2)**(0.5)
print(f'Расстояние между точками A и B = {round(result, 2)}')
