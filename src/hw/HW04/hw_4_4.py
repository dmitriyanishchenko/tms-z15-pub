# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1

my_list = [1, 'a', 3.5, 7, False, 'b', True, -10, -2]
new_list = []
i = 0
my_list_len = len(my_list)
while i <= my_list_len:
    if i + 1 == my_list_len:
        new_list.append(my_list[0])
    else:
        new_list.append(my_list[i+1])
    i += 1
while i < my_list_len - 1:
    new_list.append(my_list[i+1])
    i += 1
new_list.append(my_list[0])

print(new_list)

new_list = my_list[1:]
new_list.append(my_list[0])
print(new_list)
