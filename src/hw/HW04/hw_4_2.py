# Дан список целых чисел. Подсчитать сколько четных чисел в списке.

numbers = [1, 5, 7, -10, -2]
amount = 0
i = 0
numbers_len = len(numbers)
while i < numbers_len:
    if not numbers[i] % 2:
        amount += 1
    i += 1
print(amount)
