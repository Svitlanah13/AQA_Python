""""
QA Automation Python
Homework #2
Hnatiuk Svitlana
"""


# task_1

"""
Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'
    a. за допомогою метода рядків
    b. або (тут дам підказку тому що не встигли пройти на занятті) рядок можна розвернути за допомогою list[::-1]
"""

# ex. : "tenet", козак з казок"

word = input('Please, enter your word here: ').lower()

if word == word[::-1]:
    print('+')
else:
    print('-')


word = input('Please, enter your word here: ').lower()
letters = list(word)

if letters == letters[::-1]:
    print('+')
else:
    print('-')

print('\n')


# task_2

"""
Користувач вводить текст і слово, яке потрібно знайти, якщо це слово є в тексті, вивести 'YES', інакше 'NO'
"""

text = input('Please, enter your text here: ').lower()
word = input('Please, enter your word here: ').lower()

if word in text:
    print('YES')
else:
    print('NO')

print('\n')


# task_3

"""
Написати валідатор для пошти.
Користувач вводить пошту, а програма повинна перевірити, що в пошті є символ '@' і '.',
і якщо це так, вивести "YES", інакше "NO"
    a. можна зробити за допомогою методів рядка або за допомогою операторів приналежності
"""

email = input('Please, enter your Email here: ')

if '@' and '.' in email:
    print('YES')
else:
    print('NO')

print('\n')


# task_4

"""
Користувач вводить текст через пробіл. Конвертувати текст у список.
Вивести останні 3 елементи зі списку, якщо список містить менше 3-х елементів,
вивести повідомлення про те що кількість елементів менша за 3 і вказати кількість елементів поточного списку
"""

text = input('Please, enter your text here: ').lower()
split_text = text.split()

if len(split_text) < 3:
    print(f'This list has less than 3 elements. It has only {len(split_text)}.')
else:
    print(split_text[-3:])