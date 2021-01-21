"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

https://drive.google.com/file/d/1z8i3oJpNB_fDwfRs7bafWT3zRyCdF7zG/view?usp=sharing
"""

print('Введите трехзначное число: ')
num = int(input())
a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
summ = a + b + c
multi = a * b * c
print(f'{summ=}, {multi=}')
