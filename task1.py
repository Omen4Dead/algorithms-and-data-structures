"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import defaultdict

company_count = int(input('Введите кол-во компаний: '))
default_count = 0
dictionary = defaultdict(list)
average_company_profit = defaultdict(int)
all_profit = 0

while default_count < company_count:
    name = input('Введите название предприятия: ')
    print('Введите квартальную прибыль (4 числа): ')

    for i in range(1, 5):
        num = int(input(f'{i} квартал: '))
        dictionary[name].append(num)
        all_profit += num
        average_company_profit[name] += num

    default_count += 1

average_all_profit = all_profit / company_count
print(f'Средняя прибыль:{average_all_profit}')

# позже оптимизировать вывод на экран
for company, profit in average_company_profit.items():
    if average_company_profit[company] > average_all_profit:
        print(f'{company:<10} --> {profit}')
print('-' * 50)
for company, profit in average_company_profit.items():
    if average_company_profit[company] < average_all_profit:
        print(f'{company:<10} --> {profit}')
