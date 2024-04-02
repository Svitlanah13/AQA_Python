""""
QA Automation Python
Homework #8
Hnatiuk Svitlana
"""


# task_1

"""
Відкрити файл test_file.csv, прочитати його, зп співробітників у доларах перевести в гривні на поточну дату
(курс задається окремою змінною). Результат зберегти новий файл salaries_uah.csv
"""

import os
import csv


file_path = os.path.dirname(os.path.abspath(__file__))

file_name = 'test_file.csv'
input_file_path = os.path.join(file_path, file_name)

exchange_rate = 39.16

output_file_name = 'salaries_uah.csv'
output_file_path = os.path.join(file_path, output_file_name)

with open(input_file_path, mode='r', newline='') as input_file, \
        open(output_file_path, mode='w', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    headers = next(csv_reader)
    csv_writer.writerow(headers)

    for row in csv_reader:
        employee_name = row[0]
        salaries_usd = [int(salary) for salary in row[1:]]
        salaries_uah = [round(salary_usd * exchange_rate) for salary_usd in salaries_usd]
        csv_writer.writerow([employee_name] + salaries_uah)

print('Conversion completed and saved to salaries_uah.csv file.')

