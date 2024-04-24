""""
QA Automation Python
Homework #12
Hnatiuk Svitlana
"""

from abc import ABC, abstractmethod

# task_1

"""
Створіть абстрактний клас AbstractDevice з двома абстрактними методами: turn_on та turn_off.
Створіть клас-нащадок ConcreteDevice від абстрактного класу AbstractDevice,
який реалізовуватиме абстрактні методи батьківського класу.
"""

class AbstractDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class ConcreteDevice(AbstractDevice):
    def turn_on(self):
        print('This ConcreteDevice is turned on!')

    def turn_off(self):
        print('This ConcreteDevice is turned off!')



concrete_device = ConcreteDevice()
concrete_device.turn_on()
concrete_device.turn_off()

print('\n')


# task_2

"""
Створіть класи TV, Lights, Heating, кожен з яких має методи turn_on і turn_off для управління станом системи.
Створіть клас HomeFacade, який буде простим інтерфейсом для управління домом і буде інкапсулювати екземпляри класів TV,
Lights, Heating. Реалізуйте методи come_home і go_out у класі HomeFacade, які будуть викликати
методи включення та відключення у відповідних системах.
"""

class TV:

    def turn_on(self):
        print('TV is turned on!')

    def turn_off(self):
        print('TV is turned off!')

class Lights:

    def turn_on(self):
        print('Lights is turned on!')

    def turn_off(self):
        print('Lights is turned off!')

class Heating:

    def turn_on(self):
        print('Heating is turned on!')

    def turn_off(self):
        print('Heating is turned off!')

class HomeFacade():

    def __init__(self):
        self.tv = TV()
        self.lights = Lights()
        self.heating = Heating()

    def come_home(self):
        self.tv.turn_on()
        self.lights.turn_on()
        self.heating.turn_on()

    def go_out(self):
        self.tv.turn_off()
        self.lights.turn_off()
        self.heating.turn_off()



home = HomeFacade()
home.come_home()
home.go_out()

print('\n')


# task_3

"""
Створіть власний клас контекстного менеджера MyContextManager, який дозволить управління ресурсом з використанням конструкції with.
Реалізуйте методи __enter__ і __exit__ для власного контекстного менеджера. Наприклад, контекстний менеджер може відкривати файл
у методі __enter__ і закривати його у методі __exit__.
"""

class MyContextManager:

    def __init__(self, file_path: str, mode: str):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file = open(file=self.file_path, mode=self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


path = '/Users/svitlanahnatiuk/AQA_Python/Homeworks/homework_3.py'

with MyContextManager(file_path=path, mode='r') as file:
    print(file.readlines())