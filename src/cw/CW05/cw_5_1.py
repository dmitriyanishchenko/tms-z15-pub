# Получить сумму кубов первых n натуральных чисел используя цикл while

n = int(input('--> '))
i = 1
summ = 0
while i <= n:
    summ += i ** 3
    i += 1
print(summ)
