"""
3. По введенным пользователем координатам двух точек вывести уравнение прямой вида
y = kx + b, проходящей через эти точки.

https://drive.google.com/file/d/1z8i3oJpNB_fDwfRs7bafWT3zRyCdF7zG/view?usp=sharing
"""

print('Введите координаты первой точки (х1, у1): ')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

print('Введите координаты второй точки (x2, y2): ')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

if (y1-y2 == 0) and (x1 - x2 == 0):
    print('Невозможно построить прямую')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'Уравнение прямой:\ny = {k:.2f} * x + {b:.2f}')
