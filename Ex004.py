# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

from re import A


a = int(input('Введите число: '))

def func(a):
    b = ''
    while a > 0:
        b = str(a % 2) + b
        a = a // 2
    print(b)

func(a)