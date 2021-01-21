"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

https://drive.google.com/file/d/1z8i3oJpNB_fDwfRs7bafWT3zRyCdF7zG/view?usp=sharing
"""
print('Введите номер буквы: ')
num = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
# надеюсь, что нахождение буквы в строке по индексу не считается "работой с массивом"
char = alphabet[num - 1]
print(char)
