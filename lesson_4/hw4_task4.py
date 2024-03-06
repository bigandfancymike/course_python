# task4 - Дано лист: names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
# Використовуючи continue виведіть тілько імена у консоль

names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

# for name in names:
#     if isinstance(name, str):   #тут не дуже зрозумів, чому виводить None і 32, тому переробив з not далі
#         continue
#     print(name)

for name in names:
    if not isinstance(name, str):
        continue
    print(name)