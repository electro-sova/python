import math
import numpy as np


def first():
    a = int(input("Введите K: "))
    b = int(input("Введите М: "))
    list = []
    for i in range(a, b + 1):
        list.append(i ** 2)
    print(sum(list))

def second():
    a = int(input("Введите N: "))
    n = 1
    while math.factorial(n) < a:
        n += 1
    print(n - 1)


def third():
    for i in range(1, 10 + 1):
        print(*range(i, i * 10 + 1, i), sep='\t')


def fourth():
    a = input("Введите слово с английскими c" )
    count = 0
    for q in a:
        if q == "c":
            count += 1
    print(count)


def fifth():
    list = [1, 2, 3, 6, 2, 4, 7, 4, 2, 1]
    print(sorted(list))


def sixth():
    a = input("Введите 1 строку матрицы(5 элементов) через пробел: ").split()
    b = input("Введите 2 строку матрицы(5 элементов) через пробел: ").split()
    c = input("Введите 3 строку матрицы(5 элементов) через пробел: ").split()
    d = input("Введите 4 строку матрицы(5 элементов) через пробел: ").split()
    e = input("Введите 5 строку матрицы(5 элементов) через пробел: ").split()
    mat = np.matrix(f'{a}; {b}; {c}; {d}; {e}')
    print(mat)
    mat = np.rot90(mat)
    print(mat)


def seventh():
    a = float(input("Введите Х: "))
    b = float(input("Введите Y: "))
    dist = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    print(dist)


def eighth():
    a = int(input("Введите число, которое нужно умножить: "))
    b = int(input("Введите на сколько нужно умножить: "))
    res = 0
    for i in range(1, b + 1):
        res = res + a
    print(res)


def ninth():
    a = input("Введите число, которое хотите перевести в десятичную: ")
    print(int(a, base=2))
