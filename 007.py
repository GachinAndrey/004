# def f_gen(n):
#     temp = 1
#     for i in range(1, n + 1):
#         temp *= i
#         yield temp
#
#
# n = int(input("Укажите факториал какого числа n вы хотели бы узнать? "))
# for _ in f_gen(n):
#     print(_)

from itertools import count
from math import factorial


def f_gen():
    for i in count(1):
        yield factorial(i)


generator = f_gen()
x = 0
n = int(input("Укажите факториал какого числа n вы хотели бы узнать? "))
for i in generator:
    if x < n:
        print(i)
        x += 1
    else:
        break
