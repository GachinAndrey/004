from itertools import count
from itertools import cycle

# integer generator
for i in count(int(input("Введите стартовое число: "))):
    if i > 10:  # the cycle is limited to 10
        break
    else:
        print(i)

# repeating elements

count = 0
my_list = [True, 'ABC', 123, None]
for i in cycle(my_list):
    if count > 10:  # the cycle is limited to 10
        break
    print(i)
    count += 1
#
