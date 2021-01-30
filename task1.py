"""
для замеров используем задачу 4 из урока 3
функция определяет, какой элемент массива повторяется чаще всего

● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""
import random
import timeit
from collections import Counter


def var1(count):
    lst = [random.randint(0, 10) for _ in range(count)]
    dictionary = dict.fromkeys(lst, 0)
    for i in lst:
        dictionary[i] += 1

    max_count = 0
    result = None
    for num, count in dictionary.items():
        if count > max_count:
            max_count = count
            result = num
    return result


def var2(count):
    lst = [random.randint(0, 10) for _ in range(count)]
    max_count = 0
    result = None
    for i in lst:
        if lst.count(i) > max_count:
            max_count = lst.count(i)
            result = i
    return result


def var3(count):
    lst = [random.randint(0, 10) for _ in range(count)]
    counter = Counter(lst)

    max_count = 0
    result = None
    for num, count in counter.items():
        if count > max_count:
            max_count = count
            result = num
    return result


# самописный вариант со словарем. O(n)
print(timeit.timeit('var1(500)', number=100, globals=globals()))  # 0.09779306699965673
print(timeit.timeit('var1(1000)', number=100, globals=globals()))  # 0.12411588599934475
print(timeit.timeit('var1(2000)', number=100, globals=globals()))  # 0.22140024899999844
print(timeit.timeit('var1(4000)', number=100, globals=globals()))  # 0.5663969320003162
print(timeit.timeit('var1(8000)', number=100, globals=globals()))  # 0.9323054959995716
print(timeit.timeit('var1(100_000)', number=100, globals=globals()))  # 10.66954168600023
print()

# самописный вариант с использованием метода count. O(n**2)
print(timeit.timeit('var2(500)', number=100, globals=globals()))  # 0.5585002500001792
print(timeit.timeit('var2(1000)', number=100, globals=globals()))  # 2.1654068829993776
print(timeit.timeit('var2(2000)', number=100, globals=globals()))  # 7.8156234680000125
print(timeit.timeit('var2(4000)', number=100, globals=globals()))  # 28.51948078500027
print(timeit.timeit('var2(8000)', number=100, globals=globals()))  # 112.98408181000013
print()

# использование метода Counter из модуля collections. O(n)
# незначительно быстрее первого варианта
print(timeit.timeit('var3(500)', number=100, globals=globals()))  # 0.06468863699956273
print(timeit.timeit('var3(1000)', number=100, globals=globals()))  # 0.13677251300032367
print(timeit.timeit('var3(2000)', number=100, globals=globals()))  # 0.21274818799975037
print(timeit.timeit('var3(4000)', number=100, globals=globals()))  # 0.42525665600078355
print(timeit.timeit('var3(8000)', number=100, globals=globals()))  # 0.8022199200004252
print(timeit.timeit('var3(100_000)', number=100, globals=globals()))  # 9.919873517001179
