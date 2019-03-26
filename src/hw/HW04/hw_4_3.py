# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа 
# Пример {‘key’: ‘value’} -> {‘key3’: ‘value’}. 
# Чтобы получить список ключей - использовать метод .keys()

my_dict = {'first': 'value one', 'second': 'value two', 'third': 'value three'}

keys = list(my_dict)
i = 0
keys_len = len(keys)
while i < keys_len:
    new_key = f'{keys[i]}{len(keys[i])}'
    my_dict[new_key] = my_dict.pop(keys[i])
    i += 1
print(my_dict)

