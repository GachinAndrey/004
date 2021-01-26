from functools import reduce


def my_func(j, i):
    return j * i


print(f'Список четных значений {[i for i in range(100, 1001) if i % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [i for i in range(100, 1001) if i % 2 == 0])}')
#
