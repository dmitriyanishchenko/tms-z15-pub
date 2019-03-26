# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.

from random import randint

n = int(input('n: '))

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(str(randint(1, 9)))
    matrix.append(row)
print(matrix)

for i in range(n):
    row = ' '.join(matrix[i])
    print(row)
