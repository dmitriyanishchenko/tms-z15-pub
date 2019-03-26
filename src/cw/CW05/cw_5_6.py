# Создать квадратную матрицу размерностью n и заполнить ее 
# случайными значениями. Найти сумму всех элементов матрицы,
# которые кратны 3.

from random import randint

n = int(input('n: '))

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(randint(1, 9))
    matrix.append(row)
print(matrix)

summ = 0
for i in range(n):
    for j in range(n):
        if not matrix[i][j] % 3:
            summ += matrix[i][j]
print(summ)

