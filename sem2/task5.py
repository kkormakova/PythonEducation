# Реализуйте алгоритм перемешивания списка.

import random
list = []
for i in range(random.randint(3, 10)):
    list.append(random.randint(0, 100))
print(f'Исходный список: {list}')
random.shuffle(list)
print(f'Перемешанный список: {list}')
