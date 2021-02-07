import random
from collections import Counter
import sys

"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""
# Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
"""
   ДЗ №4 задача №3
   функция определяет, какой элемент массива повторяется чаще всего
"""


def show(obj):
    global all_memory

    # вывод на экран данных о каждой переменной
    # print(f'{type(obj)=}\t{sys.getsizeof(obj)=}\t{obj=}')

    all_memory += sys.getsizeof(obj)
    size = sys.getsizeof(obj)

    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                size += show(key)
                size += show(value)
        elif not isinstance(obj, str):
            for item in obj:
                size += show(item)

    return size


def var1(count):
    lst = [random.randint(0, 10) for _ in range(count)]
    dictionary = dict.fromkeys(lst, 0)
    for i in lst:
        dictionary[i] += 1

    max_count = 0
    result = None
    for number, count in dictionary.items():
        if count > max_count:
            max_count = count
            result = number

    for key, val in locals().items():
        show(val)

    return result


def var2(count):
    lst = [random.randint(0, 10) for _ in range(count)]
    max_count = 0
    result = None
    for i in lst:
        if lst.count(i) > max_count:
            max_count = lst.count(i)
            result = i

    for key, val in locals().items():
        show(val)

    return result


def var3(count):
    lst = [random.randint(0, 10) for _ in range(count)]
    counter = Counter(lst)

    max_count = 0
    result = None
    for number, count in counter.items():
        if count > max_count:
            max_count = count
            result = number

    for key, val in locals().items():
        show(val)

    return result


if __name__ == '__main__':
    numbers = [10, 100, 500, 1000, 2000, 4000]
    for num in numbers:
        all_memory = 0
        print(f'result for {num:<5} = {var1(num)=:<3}', f'{all_memory=:>10}')
        all_memory = 0
        print(f'result for {num:<5} = {var2(num)=:<3}', f'{all_memory=:>10}')
        all_memory = 0
        print(f'result for {num:<5} = {var3(num)=:<3}', f'{all_memory=:>10}\n')

    for _ in range(5):
        all_memory = 0
        print(f'result for {numbers[3]:<5} = {var1(numbers[3])=:<3}', f'{all_memory=:>10}')


# на малых значениях функция var2 незначительно лучше остальных в потреблении памяти,
# но в замерах скорости выполнения имеет асимптотику O(n^2)
"""
result for 10    = var1(num)=2   all_memory=      1404
result for 10    = var2(num)=7   all_memory=       576
result for 10    = var3(num)=4   all_memory=      1344

result for 100   = var1(num)=8   all_memory=      5068
result for 100   = var2(num)=10  all_memory=      3796
result for 100   = var3(num)=2   all_memory=      5080

result for 500   = var1(num)=9   all_memory=     19436
result for 500   = var2(num)=6   all_memory=     18144
result for 500   = var3(num)=0   all_memory=     19348

result for 1000  = var1(num)=6   all_memory=     37852
result for 1000  = var2(num)=10  all_memory=     36672
result for 1000  = var3(num)=1   all_memory=     37876

result for 2000  = var1(num)=4   all_memory=     72820
result for 2000  = var2(num)=5   all_memory=     71592
result for 2000  = var3(num)=3   all_memory=     72880

result for 4000  = var1(num)=3   all_memory=    144972
result for 4000  = var2(num)=5   all_memory=    143800
result for 4000  = var3(num)=9   all_memory=    144928
"""

# прогоняя код по несколько раз результат незначительно отличается
# предполагаю, что из-за разных значений в счетчиках и при генерации массива
"""
result for 1000  = var1(numbers[3])=1   all_memory=     37888
result for 1000  = var1(numbers[3])=5   all_memory=     37884
result for 1000  = var1(numbers[3])=1   all_memory=     37896
result for 1000  = var1(numbers[3])=7   all_memory=     37864
result for 1000  = var1(numbers[3])=5   all_memory=     37876
"""