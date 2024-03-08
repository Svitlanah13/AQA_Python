"""
QA Automation Python
Homework #2
Hnatiuk Svitlana
"""

# task_1

"""
Написати програму, яка вміє переводити температуру з C в Фаренгейти і Кельвіни.
Наприклад: дана температура в Цельсіях 25 С
Фаренгейт: 45.9F - вважається за формулою C * 9/5 + 32
Кельвіни: 298.16K - вважається за формулою C + 273.15
Користувач вводить температуру в градусах Цельсіях, програма виводить температуру в Фаренгейтах та Кельвінах.
"""

temperature_C = float(input('Enter temperature in Celsius: '))
print(f'{temperature_C} Celsius = {temperature_C * 9/5 + 32} Fahrenheit = {temperature_C + 273.15} Kelvin')

print(f'\n')


# task_2

"""
Змішано V1 літрів води з температурою T1 та V2 літрів з температурою T2.
Написати програму, яка порахує об'єм і температуру суміші, що вийшла.
Обчислюється за формулою (v1 * t1 + v2 * t2) / (v1 + v2).
Всі параметри виводяться в консолі, вивести обʼєм та температуру.
"""

V1 = float(input('Enter liters of water for case 1: '))
T1 = float(input('Enter temperature for case 1: '))
V2 = float(input('Enter liters of water for case 2: '))
T2 = float(input('Enter temperature for case 2: '))

new_volume = V1 + V2
new_temperature = (T1 * V1 + T2 * V2) / (V1 + V2)

print(f'Liters of water_1 = {V1}, temperature_1 = {T1} \n'
      f'Liters of water_2 = {V2}, temperature_2 = {T2} \n'
      f'Full volume of new mixture = {new_volume} \n'
      f'Temperature of new mixture = {new_temperature}')

print(f'\n')


# task_3

"""
Написати калькулятор з основними операціями (+, -, *, /).
Користувач вводить два числа та арифметичну операцію
(ви можете використовувати 2 виклики built-in функції input з різними промтами).
Підказка: input буде вам повертати "+"/"-", etc. на нього і робіть умову для if. 
Також можна додати перевірку для всіх задач з негативним сценарієм.
"""

number_1 = float(input('Enter number 1: '))
number_2 = float(input('Enter number 2: '))
operator = input('Enter operator: ')

if operator == '+':
    print(f'{number_1} {operator} {number_2} = {number_1 + number_2}')
elif operator == '-':
    print(f'{number_1} {operator} {number_2} = {number_1 - number_2}')
elif operator == '*':
    print(f'{number_1} {operator} {number_2} = {number_1 * number_2}')
elif operator == '/':
    print(f'{number_1} {operator} {number_2} = {number_1 / number_2}')
else:
    print('Sorry! I can not recognise this operator.')