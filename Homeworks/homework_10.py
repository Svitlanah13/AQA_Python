""""
QA Automation Python
Homework #10
Hnatiuk Svitlana
"""


# task_1

"""
Створіть декоратор, який повертає результат функції, а також час за який вона виконана
"""

import time

def decorator(func):

    def wraps():
        start_time = time.time()
        result = func()
        end_time = time.time()

        print(f'Function was executed in {end_time - start_time}!')

        return result

    return wraps

@decorator
def sum_range():
    print(f'Result is: {sum(range(350))}')

sum_range()

print('\n')


# task_2

"""
Створіть декоратор, котрий приймає аргумент, аргумент повинен бути рядком та роздрукований за допомогою print
перед виконанням функції (тобто зробимо примітивний логер).
    Наприклад
    @logger('This function will sum 2 ints')
    def plus(x, y):
        return x + y
    Виклик та вивід:
    plus(10, 20)
    This function will sum 2 ints
    30
"""

def logger(string):
    def decorator(func):
        def wraps(*args, **kwargs):
            print(string)
            return func(*args, **kwargs)
        return wraps
    return decorator

@logger('This function will sum all integer numbers from start value to end value.')
def sum_range(start, end):

    if start > end:
        start, end = end, start

    integer_numbers = [number for number in range(start, end+1)]
    total_sum = sum(integer_numbers)
    return f'Result: Sum from {start} to {end} is {total_sum}.'

result = sum_range(45,19)
print(result)