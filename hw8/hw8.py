import csv


currency_exchange_rate = 39

with open('test_file.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    users_salaries = list(csv_reader)
    months = users_salaries[0]
    salaries_uah = []

    for row in users_salaries[1:]:
        employee = row[0]
        salaries = [int(salary) * currency_exchange_rate for salary in row[1:]]
        salaries.insert(0, employee)
        salaries_uah.append(salaries)

with open('salaries_uah.csv', mode='w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(months)
    csv_writer.writerows(salaries_uah)
