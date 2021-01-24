"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
   Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

https://drive.google.com/file/d/1oD1WqLZUqJkGgDCthhYxKxHULn00i8c5/view?usp=sharing
"""

print('Введите натуральное целое число: ')
num = input('num = ')

odd_num = 0
even_num = 0

for i in num:
    if int(i) % 2 == 0:
        even_num += 1
    else:
        odd_num += 1

print(f'Четные числа: {even_num}')
print(f'Нечетные числа: {odd_num}')
