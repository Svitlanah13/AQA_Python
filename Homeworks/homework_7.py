""""
QA Automation Python
Homework #7
Hnatiuk Svitlana
"""


# task_1

"""
Напишіть самостійно функції котрі буде повторювати поведінку built-in функції
    a. map 
    b. filter
"""

def own_map(func, iterable):
    result = []
    for element in iterable:
        result.append(func(element))
    return result


def own_filter(func, iterable):
    result = []
    for element in iterable:
        if func(element):
            result.append(element)
    return result


# task_2

"""
Напишіть функцію котра приймає 1 аргумент (int)(нехай це буде х) та повертає lambda функцію
котра приймає один аргумент (нехай буде y) котрий буде піднесений до ступеня аргументу з функції (def),
тобто змінна y буде піднесена до ступеня змінної х
"""

def lambda_function(x: int):
    return lambda y: y ** x

my_func = lambda_function(2)
print(my_func(3))

print('\n')


# task_3

"""
Напишіть програму котра буде приймати назву функцій з консолі (input) (вони повинні існувати)
та за допомогою built-in функції виводьте результат виконання переданої функції
"""

def greet():
    print('Hello, user!')

def wish():
    print('Have a nice day!')

def evaluate():
    user_input = input('Enter function name: ')
    eval(user_input + '()')

evaluate()