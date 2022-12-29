# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите число X')
x = int(input())
print('Введите число Y')
y = int(input())
print('Введите число Z')
z = int(input())
left = not (x or y or z)
right = not x and not y and not z
if left == right:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
