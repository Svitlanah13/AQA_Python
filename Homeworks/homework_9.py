""""
QA Automation Python
Homework #9
Hnatiuk Svitlana
"""


# task_1

"""
Напишіть генератор котрий буде працювати як range() із агрументами start, stop & step
"""

def generator(start: int, stop: int, step: int):

    value = start
    while value < stop:
        yield value
        value += step

for element in generator(0, 100, 2):
    print(element)

print('\n')


# task_2

"""
Напишіть generator comprehansion котрий буде повертати числа від 1 до 10
"""

generator_comp = (num for num in range(1, 10+1))

for element in generator_comp:
    print(element)