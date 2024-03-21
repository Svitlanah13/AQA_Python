""""
QA Automation Python
Homework #6
Hnatiuk Svitlana
"""


# task_1

"""
Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно.
Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями.
"""

def sum_range(start, end):

    if start > end:
        start, end = end, start

    integer_numbers = [number for number in range(start, end+1)]
    total_sum = sum(integer_numbers)
    #print(f'Result: Sum from {start} to {end} is {total_sum}.')

sum_range(45,19)
sum_range(20,87)

print('\n')


# task_2

"""
Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення : периметр квадрата,
площа квадрата та діагональ квадрата. Надрукуйте їх.
"""

import math

def square(square_side):

    square_perimeter = 4 * square_side
    square_area = square_side ** 2
    diagonal = square_side * math.sqrt(2)

    return f'Perimeter: {square_perimeter}. Area: {square_area}. Diagonal: {diagonal:.2f}'

print(square(8))

print('\n')

# task_3

"""
Напишіть 2 функції котрі:

1. Приймає ввід від юзера з консолі та повертає введене значення, приклад вводу 
    1.1 ['name', 1, 2]
    1.2 ('there', 'is', 'tuple')
    1.3 {'country': 'Ukraine', 'city': 'Kyiv'} 
    1.4 100

2. Приймає результат виконання першої функції та друкує повідомлення у консоль
"User is going to work with (there is data type)"
(тут треба за допомогою try except намагатись перетворити отриманий аргумент у dict, int, list, tuple)
"""

def take_data_from_user():
    user_data = input('Enter here your data: ')
    return user_data


def type_of_user_data(data):
    try:
        data_type = type(eval(data))
        print(f"User is going to work with {data_type}")
    except Exception as e:
        print(f"Error: {e}")


user_input = take_data_from_user()
type_of_user_data(user_input)