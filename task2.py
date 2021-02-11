"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
import random


# интересный алгоритм с понятной идеей, но самостоятельно в коде я его вряд-ли смогу повторить)))
def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        right = array[middle:]
        left = array[:middle]

        merge_sort(right)
        merge_sort(left)

        i, j, k = 0, 0, 0

        while i < len(right) and j < len(left):
            if left[j] > right[i]:
                array[k] = right[i]
                i += 1
            else:
                array[k] = left[j]
                j += 1
            k += 1

        while i < len(right):
            array[k] = right[i]
            i += 1
            k += 1

        while j < len(left):
            array[k] = left[j]
            j += 1
            k += 1
    return array


lst = [random.uniform(0, 50) for _ in range(10)]
print(lst)
merge_sort(lst)
print(lst)
