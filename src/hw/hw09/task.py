
# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.

list_a = ['dog', 'cat', 'rat']
list_b = [f'{i} - {elem}' for i, elem in enumerate(list_a)]
print(list_b)


# Создать lambda функцию, которая принимает на вход неопределенное количество именных
# аргументов и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}

my_dict = {'a': 24, 'b': 33}
print((lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(**my_dict))



# Создать декоратор для функции, который принимает список чисел.
# Декоратор должен производить предварительную проверку данных - 
# удалять все четные элементы из списка. 

def even_args(func):
    def wrapper (*args, **kwargs):
        args = [elem for elem in args if elem % 2 != 0]
        return func(*args, **kwargs)
    return wrapper

@even_args
def print_args(*args):
   print(args)


my_list = [1, 2, 3, 4]
print_args(*my_list)


# Создать универсальны декоратор,
# который меняет порядок аргументов 
# в функции на противоположный.

def backwards_args(func):
    def wrapper (*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return wrapper


@backwards_args
def print_my_args(*args):
   print(args)


print_my_args(1, 2, 3, 4)