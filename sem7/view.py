#Взаимодействие с пользователем

def choise():
    action = int(input('Введите номер команды: \n1 - Сделать запись\n2 - Получить номер телефона\n3 - Удалить запись\n'))
    if action == 1:
        text_input = input('Введите ФИО и номер телефона через пробел:\n')
        return (text_input, action)
    elif action == 2:
        text_input = input('Введите Фамилию/Имя/Отчество:\n')
        return (text_input, action)
    elif action == 3:
        text_input = input('Введите Фамилию/Имя/Отчество/Номер телефона:\n')
        return (text_input, action)


def res_find(string: list):
    for item in string:
        print(item)