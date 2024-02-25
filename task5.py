"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

https://drive.google.com/file/d/1z8i3oJpNB_fDwfRs7bafWT3zRyCdF7zG/view?usp=sharing
"""
a1 = input('Введите первую букву: ')
a2 = input('Введите вторую букву: ')

alphabet = "abcdefghijklmnopqrstuvwxyz"
a1 = a1.lower()
a2 = a2.lower()
ind_a1 = alphabet.find(a1) + 1
ind_a2 = alphabet.find(a2) + 1
print('Индекс первой буквы, индекс второй буквы, кол-во букв между ними:')
print(ind_a1, ind_a2, (abs(ind_a2 - ind_a1)) - 1)
