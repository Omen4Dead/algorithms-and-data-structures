"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
   Например, если введено число 3486, надо вывести 6843.

https://drive.google.com/file/d/1oD1WqLZUqJkGgDCthhYxKxHULn00i8c5/view?usp=sharing
"""
print('Введите натуральное целое число')
num = int(input())
result = ''


def turn(res, n):
    ost = str(n % 10)
    res += ost
    if n > 10:
        return turn(res, n // 10)

    return int(res)


a = turn(result, num)
print(a)
