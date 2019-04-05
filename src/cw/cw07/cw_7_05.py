# Создать функцию, принимающая на вход неопределенное количество 
# аргументом и возвращающая сумму args[i] * i
# Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10


def sum_func(*args):
    summ = 0
    for i, elem in enumerate(args):
        summ += elem * i
    return summ

print(sum_func(4,3,2,1))