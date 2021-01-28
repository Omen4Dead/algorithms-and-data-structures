"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
FIRST = 2
LAST = 99

res_dict = dict.fromkeys(range(2, 10), 0)  # создание словаря
print(res_dict)

for i in range(FIRST, LAST):
    for j in range(2, 10):
        if i % j == 0:
            res_dict[j] += 1

print(res_dict)
