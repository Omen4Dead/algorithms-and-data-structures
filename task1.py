"""
1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.

Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
p a pa ap pap apa
6

func("sova")
s o v a so ov va sov ova
9

func("maria")
m a r i ma ar ri ia mar ari ria mari aria
13
"""
import hashlib


def func(n):
    if len(n) == 0 or len(n) == 1:
        return len(n)
    result = set()
    count = 1
    while count < len(n):
        for i in range(len(n)):
            result.add(hashlib.sha1(n[i:i + count].encode('utf-8')).hexdigest())
        count += 1
    return len(result)


def func_no_hash(string):
    count = 1
    container = set()
    while count < len(string):
        spam = [string[x:x + count] for x in range(0, len(string)) if len(string[x:x + count]) == count]
        for i in spam:
            container.add(i)
        count += 1
    return len(container)


print(func_no_hash('papa'))
print(func_no_hash('sova'))
print(func_no_hash('maria'))
print(func('papa'))
print(func('sova'))
print(func('maria'))
