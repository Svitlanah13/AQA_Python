""""
QA Automation Python
Homework #2
Hnatiuk Svitlana
"""


# task_1

"""
1. Створи клас котрий буде мати class & instance attributes, getter & setter
2. Створити клас котрий буде успадковувати клас з першого завдання, та додати новий метод у CHILD клас
Приклад:
Є клас Ship котрий має різні атрибути та метод move, потрібно створити клас Lainer котрий буде успадковувати Ship
та мати метод entertaiment та, наприклад просто виводи у консоль 'Watch movie'
Якщо будуть додаткові питання то пишіть у особисті або у загальний чат =)
Та будь ласка не забувайте про doc-string, зрозумілі назви методів та класів, та Style Guide (PEP-8)
"""

class Ship:

    def __init__(self, type: str, speed: int):
        self.type = type
        self.speed = speed

    def get_type(self):
        return self.type

    def set_speed(self, value: int):
        if value <= 0:
            return 'This machine is not active'
        elif value >= 40:
            return 'We have to reduce the speed'
        else:
            self.speed = value


class Lainer(Ship):

    def __init__(self, type: str, speed: int):
        super().__init__(type, speed)

    def entertaiment(self):
        print('Bowling')
