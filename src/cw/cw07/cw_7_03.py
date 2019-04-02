# Написать программу для работы с матрицами: создание, вывод, 
# сумма всех элементов, нахождение максимального, минимального элемента.

from random import randint


def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(randint(1, 9))
        matrix.append(row)
    return matrix

a = create_matrix(5)
print(a)
def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()

def sum_matrix(matrix):
    summ = 0
    for row in matrix:
        for elem in matrix:
            summ += elem
    return summ

def get_max_elem(matrix):
    max_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > max_elem:
                max_elem = elem
    return max_elem

def get_min_elem(matrix):
    min_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < min_elem:
                min_elem = elem
    return min_elem


matrix_a = create_matrix(5)
print_matrix(matrix_a)
print(get_max_elem(matrix_a))
print(get_min_elem(matrix_a))