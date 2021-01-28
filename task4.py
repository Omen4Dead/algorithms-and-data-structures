"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

SIZE = 20
MIN_ITEM = 3
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

dictionary = dict.fromkeys(array, 0)
print(dictionary)

for i in array:
    dictionary[i] += 1

print(dictionary)

max_count = 0
result = None
for num, count in dictionary.items():
    if count > max_count:
        max_count = count
        result = num

print(result, '-->', max_count)
