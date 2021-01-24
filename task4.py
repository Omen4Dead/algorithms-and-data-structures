"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
   Количество элементов (n) вводится с клавиатуры.

https://drive.google.com/file/d/1oD1WqLZUqJkGgDCthhYxKxHULn00i8c5/view?usp=sharing
"""
print('Введите натуральное число: ')
n = int(input())
i = 1
summa = 1
count = 0
while count < n:
    i = (i / 2) * -1
    summa += i
    count += 1

print(f'{summa=}')
