"""
QA Automation Python
Homework #5
Hnatiuk Svitlana
"""


# task_1

"""
Написати програму, яка запитує у користувача число і обчислює його квадратний корінь.
Передбачити обробку винятку, який виникає при спробі обчислення квадратного кореня з від'ємного числа,
і вивести відповідне повідомлення. (Тут потрібно додати перевірку на відʼємне число та якщо воно дійсно таке,
то спонукати помилку за допомогою ключового слова raise, та створіть свою помилку котра будете спонукати).
Використати else для виведення результату, якщо обчислення пройшло успішно.
Додати конструкцію finally, яка виводитиме повідомлення про завершення операції обчислення.
"""

import math

class NegativeNumber(Exception):
    pass

def calculate_square_root():
    try:
        number = float(input('Please enter your number here: '))
        if number < 0:
            raise NegativeNumber(f'You cannot find the square root of {number}, it is a negative number.')
        else:
            result = math.sqrt(number)
            print(f'Your calculation is successful: Square root of {number} = {result}')
    except NegativeNumber as e:
        print(e)
    finally:
        print('This operation is done!')

calculate_square_root()

print('\n')


# task_2

"""
Модифікувати попередню програму так, щоб вона також обробляла помилку введення,
коли введене значення не може бути перетворене на число (ValueError),
виводячи користувачеві зрозуміле повідомлення про помилку. (потрібно написати ще одну програму.
"""

def holding_value_error_in_sqrt():
    try:
        number = int(input('Please enter your number here: '))
        if number < 0:
            raise NegativeNumber(f'You cannot find the square root of {number}, it is a negative number.')
        else:
            result = math.sqrt(number)
            print(f'Your calculation is successful: Square root of {number} = {result}')
    except ValueError:
        print('Please enter a valid value.')
    except NegativeNumber as e:
        print(e)
    finally:
        print('This operation is done!')

holding_value_error_in_sqrt()

print('\n')


# task_3

"""
Розширити роботу нашого калькулятора, додавши можливість користувачеві вводити числа до тих пір,
поки він не вирішить вийти, вводячи певне ключове слово (наприклад, "вихід").
Забезпечити коректну обробку введення для виходу з програми без виникнення помилок.
Використовуйте try, except, else, finally для обробки можливих винятків.
"""

attempts_counter = 0

while attempts_counter < 2:

    try:
        number_1 = input('Enter number 1: ')
        if number_1.lower() == 'exit':
            raise KeyboardInterrupt
        if number_1.isdigit():
            number_1 = int(number_1)
        else:
            raise ValueError('Entered value is not digit')

        number_2 = input('Enter number 2: ')
        if number_2.lower() == 'exit':
            raise KeyboardInterrupt
        if number_2.isdigit():
            number_2 = int(number_2)
        else:
            raise ValueError('Entered value is not digit')

        operator = input('Enter operator (+, -, *, /): ')
        if operator.lower() == 'exit':
            raise KeyboardInterrupt

        if operator not in ['+', '-', '*', '/']:
            raise ValueError('Not recognised operator')

        if operator == '/' and number_2 == 0:
            raise ZeroDivisionError('You can not division by zero')

        if operator == '+':
            result = number_1 + number_2
        elif operator == '-':
            result = number_1 - number_2
        elif operator == '*':
            result = number_1 * number_2
        elif operator == '/':
            result = number_1 / number_2

        print(f'Result: {number_1} {operator} {number_2} = {result}')
        attempts_counter = 0

    except KeyboardInterrupt:
        print('Exiting the calculator by user decision.')
        break

    except (ValueError, ZeroDivisionError) as e:
        attempts_counter += 1
        print(f'Error: {e}. Please try again.\n')

    except Exception as e:
        attempts_counter += 1
        print(f'Unexpected error occurred: {e}. Please try again.\n')

    finally:
        print('End of calculation.\n')

else:
    print('Sorry, there are no attempts left. Exiting the calculator.')

