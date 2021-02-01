"""
для замеров используем задачу 4 из урока 3
функция определяет, какой элемент массива повторяется чаще всего
"""
import random
import timeit
from collections import Counter
import cProfile


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

print(timeit.timeit('var1(500)', number=100, globals=globals()))  # 0.03980587099977129
print(timeit.timeit('var1(1000)', number=100, globals=globals()))  # 0.08470900700012862
print(timeit.timeit('var1(2000)', number=100, globals=globals()))  # 0.16483540299986998
print(timeit.timeit('var1(4000)', number=100, globals=globals()))  # 0.31264069600001676
print(timeit.timeit('var1(8000)', number=100, globals=globals()))  # 0.608461115999944
print(timeit.timeit('var1(100_000)', number=100, globals=globals()))  # 7.586634065999988
print()

# самописный вариант с использованием метода count. O(n**2)

print(timeit.timeit('var2(500)', number=100, globals=globals()))  # 0.33397618500021053
print(timeit.timeit('var2(1000)', number=100, globals=globals()))  # 1.3257236240001475
print(timeit.timeit('var2(2000)', number=100, globals=globals()))  # 5.259451552000428
print(timeit.timeit('var2(4000)', number=100, globals=globals()))  # 20.953168301999995
print(timeit.timeit('var2(8000)', number=100, globals=globals()))  # 82.76332424199973
print()

# использование метода Counter из модуля collections. O(n)
# незначительно быстрее первого варианта

print(timeit.timeit('var3(500)', number=100, globals=globals()))  # 0.035388312000122824
print(timeit.timeit('var3(1000)', number=100, globals=globals()))  # 0.07027345899996362
print(timeit.timeit('var3(2000)', number=100, globals=globals()))  # 0.14185508900027344
print(timeit.timeit('var3(4000)', number=100, globals=globals()))  # 0.2826075910002146
print(timeit.timeit('var3(8000)', number=100, globals=globals()))  # 0.5671327029999702
print(timeit.timeit('var3(100_000)', number=100, globals=globals()))  # 7.188077041999804
print()

cProfile.run('var1(1000)')
"""
   5483 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
     1000    0.001    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:244(randint)
     1000    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.002    0.002 task1.py:11(var1)
        1    0.000    0.000    0.002    0.002 task1.py:12(<listcomp>)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method fromkeys}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1476    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
"""

cProfile.run('var2(1000)')
"""
   6441 function calls in 0.015 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.015    0.015 <string>:1(<module>)
     1000    0.000    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:244(randint)
     1000    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.015    0.015 task1.py:26(var2)
        1    0.000    0.000    0.002    0.002 task1.py:27(<listcomp>)
        1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
     1001    0.013    0.000    0.013    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1435    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

cProfile.run('var3(1000)')
"""
   5495 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 __init__.py:540(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:608(update)
        1    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
     1000    0.000    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:244(randint)
     1000    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.002    0.002 task1.py:37(var3)
        1    0.000    0.000    0.001    0.001 task1.py:38(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        1    0.000    0.000    0.000    0.000 {built-in method _collections._count_elements}
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1483    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
"""
