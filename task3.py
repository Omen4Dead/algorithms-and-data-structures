"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
import random
import statistics


def find_median(array):
    for i in array:
        less_count = 0
        more_count = 0
        for j in array:
            if j < i:
                less_count += 1
            elif j > i:
                more_count += 1
        if less_count == more_count:
            return i


num = int(input('Введите натуральное число: '))
lst = [random.randint(-100, 100) for _ in range(2 * num + 1)]

# для тестов
# lst = [random.randint(-100, 100) for _ in range(11)]
print(lst)
a = find_median(lst)
print(lst)
print(statistics.median(lst))
print(a)
