import csv

# Добавление контакта


def create_data(text: str):
    text = list(text.split())
    with open('database.csv', 'a', newline='', encoding='UTF-8') as file:
        data = csv.writer(file)
        data.writerow(text)
        print('Информация внесена')
