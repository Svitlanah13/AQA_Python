""""
QA Automation Python
Homework #4
Hnatiuk Svitlana
"""

# task_1

"""
Існує список з іменами ["john", "marta", "james", "amanda", "marianna"],
перетворити рядок, щоб кожне ім'я явно починалися з великої літери.
"""

names_list = ["john", "marta", "james", "amanda", "marianna"]

capitalized_names_list = [name.capitalize() for name in names_list]

print(capitalized_names_list)

print('\n')


# task_2

"""
У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"],
перетворити його у список змінних для Пайтона snace_case, "friends_list", "my_tuple"]
"""

camel_case = ["FirstItem", "FriendsList", "MyTuple"]

for element in camel_case:
    print(''.join(['_'+letter.lower() if letter.isupper() else letter for letter in element]).lstrip('_'))

print('\n')


# task_3

"""
Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення).
Виведіть по черзі для усіх елементів словника повідомлення типу My favorite programming language is Python.
It was created by Guido van Rossum.
Видаліть, на ваш вибір, одну пару «мова: розробник» із словника. Виведіть словник на екран.
"""

programming_language = {'Java': 'James Gosling', 'PHP': 'Rasmus Lerdorf', 'C++': 'Bjarne Stroustrup', 'Python': 'Guido van Rossum'}

for key, value in programming_language.items():
    print(f'My favorite programming language is {key}. It was created by {value}.')

print('\n')

# del programming_language['C++']
programming_language.pop('C++')

print(programming_language)

print('\n')


# task_4

"""
Дан лист: names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
Використовуючи continue виведіть тілько імена у консоль.
"""

names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

for element in names:
    if type(element) is not str:
        continue
    print(element)

print('\n')


# task_5

"""
Дан лист types=[1, 1000, 2, 12, {'key': 'value'}
Використовуючи break напишіть програму котра буде виводити тільки int тип даних,
якщо тип буде інший зупинити цикл з повідомленням
f'цикл не працює з {тут тип даних із-за якого ми зупинили цикл} типом даних'
Підказка: type()
"""

types = [1, 1000, 2, 12, {'key': 'value'}]

for element in types:
    if type(element) is int:
        print(element)
    else:
        break
print(f"Cycle doesn't work with {type(element)} data type!")

print('\n')


# task_6

"""
Напишіть програму котра підраховує кількість однакових символів у значенні котре введе користувач в консолі
Приклад
Користувач вводить abcdefgabc
Очікуваний результат a,2 c,2 b,2 e,1 d,1 g,1 f,1
Підказка: Використуйте dict для збереження пари key/value.
Для виводу викоритуйте dict.get() метод з дефолтнім значенням для випадків коли ключа не існує.
Використайте str.join() метод та dict comprehension для виводу результату
"""

text = input('Enter your text here please: ')

character_number = {key: text.count(key) for key in text}

print(' '.join(f'{key},{value}' for key, value in character_number.items()))

print('\n')


# task_7

"""
Перепишіть калькулятор з минулих дз, який буде продовжувати працювати при невірно введених даних юзером.
Додаткова умова: у юзера буде всього 2 спроби ввести правильні значення,
після другої спроби програма повинна завершуватись з повідомленням Спроби скінчились.
"""

attempts = []

while len(attempts) < 2:

    number_1 = int(input('Enter number 1: '))
    number_2 = int(input('Enter number 2: '))
    operator = input('Enter operator: ')

    if operator not in '+, -, *, /':
        attempts.append(True)
        print('Sorry! We can not recognise this operator.\n')
        continue

    elif operator == '/':
        if number_2 == 0:
            attempts.append(True)
            print('You can not division by 0.\n')
            continue
        else:
            print(f'{number_1} {operator} {number_2} = {int(number_1) / int(number_2)}')

    elif operator == '+':
        print(f'{number_1} {operator} {number_2} = {int(number_1) + int(number_2)}')

    elif operator == '-':
        print(f'{number_1} {operator} {number_2} = {int(number_1) - int(number_2)}')

    elif operator == '*':
        print(f'{number_1} {operator} {number_2} = {int(number_1) * int(number_2)}')

    break

else:
    print('Sorry, there are no left attempts.')
