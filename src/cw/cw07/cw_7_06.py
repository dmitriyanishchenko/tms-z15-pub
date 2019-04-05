# Создать функцию, которая принимает на вход неопределенное количество 
# аргументов и возвращает их сумму и максимальное из них.

def sum_mux_func(*args):
    summ = 0
    max_elem = args[0]
    for elem in args:
        summ += elem
        if elem > max_elem:
            max_elem = elem
    return summ, max_elem

print(sum_mux_func(4,3,2,1))
