"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».

Второй — без использования «Решета Эратосфена».
"""
import timeit
import cProfile


def sieve(n):
    sieve_1 = [i for i in range(n*100)]
    sieve_1[1] = 0
    lst = []

    for i in range(2, n*100):
        if sieve_1[i] != 0:
            lst.append(sieve_1[i])
            if len(lst) == n:
                return lst[-1]
            j = i + i
            while j < n*100:
                sieve_1[j] = 0
                j += i


def prime(index):
    lst_result = []
    for num in range(2, index*100):
        for num2 in range(2, num):
            if num % num2 == 0:
                break
        else:
            lst_result.append(num)
            if len(lst_result) == index:
                break
    return lst_result[-1]


# судя по скорости увеличения времени функция sieve имеет сложность O(log(n))
print(timeit.timeit('sieve(50)', number=100, globals=globals()))  # 0.10428009299994301
print(timeit.timeit('sieve(100)', number=100, globals=globals()))  # 0.22928484000021854
print(timeit.timeit('sieve(200)', number=100, globals=globals()))  # 0.47490047399969626
print(timeit.timeit('sieve(400)', number=100, globals=globals()))  # 0.9653489439997429
print(timeit.timeit('sieve(800)', number=100, globals=globals()))  # 2.0032538619998377
print(timeit.timeit('sieve(1600)', number=100, globals=globals()))  # 4.281401513000219
print()
# судя по скорости увеличения времени функция prime имеет сложность O(n^2)
print(timeit.timeit('prime(50)', number=100, globals=globals()))  # 0.026629388999936054
print(timeit.timeit('prime(100)', number=100, globals=globals()))  # 0.11862703999986479
print(timeit.timeit('prime(200)', number=100, globals=globals()))  # 0.5760988050001288
print(timeit.timeit('prime(400)', number=100, globals=globals()))  # 2.759314083999925
print(timeit.timeit('prime(800)', number=100, globals=globals()))  # 12.908960523000133
print(timeit.timeit('prime(1600)', number=100, globals=globals()))  # 58.75326415299969

cProfile.run('sieve(1000)')
"""
   2005 function calls in 0.026 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.026    0.026 <string>:1(<module>)
        1    0.022    0.022    0.026    0.026 task2.py:17(sieve)
        1    0.003    0.003    0.003    0.003 task2.py:18(<listcomp>)
        1    0.000    0.000    0.026    0.026 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('prime(1000)')
"""
   2004 function calls in 0.236 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.236    0.236 <string>:1(<module>)
        1    0.236    0.236    0.236    0.236 task2.py:33(prime)
        1    0.000    0.000    0.236    0.236 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
