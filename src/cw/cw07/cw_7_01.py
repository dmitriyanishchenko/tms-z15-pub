# Написать функцию, которая получает на вход имя и
# выводит строку вида: “Hello, {name}”. Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.


def hello(name):
    print(f'Hello, {name}')

names = ['Alex', 'Max', 'Kate', 'Dima', 'Roma']

for name in names:
    hello(name)
