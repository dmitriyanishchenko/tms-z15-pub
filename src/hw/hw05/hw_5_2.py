# Для каждого натурального числа в промежутке 
# от m до n вывести все делители, кроме единицы 
# и самого числа. m и n вводятся с клавиатуры.

n = int(input('n: '))
m = int(input('m: '))

for i in range(n, m + 1 ):
    row = []
    for j in range(2, i // 2 + 1):
        if not i % j:
            row.append(str(j))
    string = f'{i}: {" ".join(row)}'
    print(string)
