# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))

def fibonacci(n):
    list = []
    a, b = 1, 1
    for i in range(n-1):
        list.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        list.insert(0, a)
        a, b = b, a - b
    return list

list = fibonacci(n)
print(fibonacci(n+1))