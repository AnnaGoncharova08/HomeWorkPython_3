# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

a = [2, 3, 5, 5, 6]
b = []
def product(a):
    for i in range((len(a)+1)//2):
        b.append(a[i] * a[len(a) - 1 - i])
    print(b)

product(a)