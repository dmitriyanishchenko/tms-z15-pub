# Написать программу для нахождения факториала. 
# Факториал натурального числа n определяется как 
# произведение всех натуральных чисел от 1 до n включительно

def factorial(n):
    i = n
    result = 1
    while i:
        result *= i
        i -= 1
    return result

print(factorial(4))
