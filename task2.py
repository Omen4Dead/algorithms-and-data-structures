"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# new_array = []
#
# for pos, number in enumerate(array):
#     if number % 2 == 0:
#         new_array.append(pos)

new_array = [pos for pos, number in enumerate(array) if number % 2 == 0]

print(new_array)
