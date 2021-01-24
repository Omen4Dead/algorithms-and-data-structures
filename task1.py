"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

https://drive.google.com/file/d/1oD1WqLZUqJkGgDCthhYxKxHULn00i8c5/view?usp=sharing
"""
while True:
    znak = input('Введите знак операции над числами:')
    if znak == '0':
        break

    if znak == '+' or znak == '/' or znak == '*' or znak == '-':
        pass
    else:
        print('Ошибка ввода')
        continue

    num1 = int(input('num1 = '))
    num2 = int(input('num2 = '))
    result = None

    if znak == '/' and num2 == 0:
        print('Ошибка: Деление на 0')
        continue
    elif znak == '+':
        result = num1 + num2
    elif znak == '-':
        result = num1 - num2
    elif znak == '*':
        result = num1 * num2
    elif znak == '/':
        result = num1 / num2

    print(result)