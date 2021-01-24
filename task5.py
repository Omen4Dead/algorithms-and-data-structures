"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

https://drive.google.com/file/d/1oD1WqLZUqJkGgDCthhYxKxHULn00i8c5/view?usp=sharing
"""
first = 32
count = 0
while first <= 127:
    if count == 10:
        count = 0
        print()
    print(f'{first:>3} -> {chr(first)} | ', end='')
    first += 1
    count += 1
