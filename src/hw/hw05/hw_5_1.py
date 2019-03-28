#Дана целочисленная матрица размера 5х5. Получить новую матрицу
#путем деления всех элементов данной матрицы на ее наибольший по
#модулю элемент.[02-4.2-ML-17]

from random import randint

matrix = []
n = int(input('--> '))
for i in range(n):
    row = []
    for j in range(n):
        row.append(randint(0, 9))
    matrix.append(row)

max_elem = 0
for i in range(n):
    for j in range(n):
        if max_elem < abs(matrix[i][j]):
            max_elem = abs(matrix[i][j])

if max_elem != 0:
    new_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(round(matrix[i][j] / max_elem, 4))
        new_matrix.append(row)
        print(row)