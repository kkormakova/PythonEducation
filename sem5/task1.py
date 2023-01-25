# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'молвкгу шгмтгудмАБВ шщцукоа абвоукг щульашиабв'
print(f'Что было: {text}')


def delword(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(text)


text = delword(text)
print(f'Что стало: {text}')
