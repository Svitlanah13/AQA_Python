""""
QA Automation Python
Homework #13
Hnatiuk Svitlana
"""


# task_1

"""
Написати Singleton (на вибір за допомогою мета класу або декоратора)
"""

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Data(metaclass=Singleton):
    def __init__(self, data):
        self.data = data

result_1 = Data('10')
result_2 = Data('1000')

print(result_1.data)
print(result_2.data)


print('\n')


def singleton(cls):
    _instances = {}

    def instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return instance


@singleton
class Data:
    def __init__(self, data):
        self.data = data

result1 = Data('Svitlana')
result2 = Data('Hnatiuk')

print(result1.data)
print(result2.data)