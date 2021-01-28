"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 20
MIN_ITEM = -1000
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# array.sort()  # для наглядности при проверке
print(array)

max_pos = 0
max_el = array[0]
min_pos = 0
min_el = array[0]

for pos, el in enumerate(array):
    if el > max_el:
        max_el = el
        max_pos = pos
    if el < min_el:
        min_el = el
        min_pos = pos

array[max_pos], array[min_pos] = array[min_pos], array[max_pos]

print(array)
