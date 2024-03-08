# task3 - Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення). Виведіть по черзі для усіх елементів словника повідомлення типу My favorite programming language is Python. It was created by Guido van Rossum.. Видаліть, на ваш вибір, одну пару «мова: розробник» із словника. Виведіть словник на екран.

# dictionary1 = {'java': 'James Gosling', 'js': 'Brendan Eich', 'ruby': 'Yukihiro Matsumoto', 'python': 'Guido van Rossum'}
#
# for language, developer in dictionary1.items():
#     print(f'My favorite programming language is Python. It was created by Guido van Rossum.')
# del dictionary1['js']
# print('Updated one:', dictionary1)

dictionary1 = {'java': 'James Gosling', 'js': 'Brendan Eich', 'ruby': 'Yukihiro Matsumoto', 'python': 'Guido van Rossum'}

for language, developer in dictionary1.items():
    print(f'My favorite programming language is {language.capitalize()}. It was created by {developer}.')
del dictionary1['js']
print('Updated one:', dictionary1)