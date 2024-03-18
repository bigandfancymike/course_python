# ### **Функції для роботи з числами**
#
# abs(x) Повертає абсолютне значення числа.
# divmod(a, b) Повертає пару, що складається з частки та залишку від ділення a на b.
# pow(x, y[, z]) Повертає x піднесене до степеня y, якщо задано z, то повертає (x ** y) % z.
# round(number[, ndigits]) Округляє число до заданої кількості знаків після коми.
#
# absolute = abs(-10)
# print(absolute)
# print(-10)
#
# div = divmod(10, 2)
# print(div)
# print(10 % 2)
# print(10 // 2)


# res = pow(10, 2)
# print(res)
#
# number = 10.2124123123
# print(round(number, 2))
#
# ### **Функції для роботи з ітерабельними об'єктами**
#
# all(iterable) Повертає True, якщо всі елементи ітерабельного об'єкта є істинними (або якщо ітерабельний об'єкт порожній).
# any(iterable) Повертає True, якщо хоча б один елемент ітерабельного об'єкта є істинним.
# filter(function, iterable) Використовує function для фільтрації елементів iterable, повертаючи ті, для яких function повертає True.
# map(function, iterable, ...) Застосовує function до кожного елементу iterable і повертає новий ітератор з результатами.
# range(start, stop[, step]) Генерує послідовність чисел від start до stop з кроком step.
# zip(*iterables) Створює ітератор, який агрегує елементи з кожного з ітерабельних об'єктів.
#
# ### **Функції для роботи з колекціями**
#
# len(s) Повертає кількість елементів у об'єкті.
# min(iterable, *[, default=obj, key=func]) Повертає найменше значення в ітерабельному об'єкті.
# max(iterable, *[, default=obj, key=func]) Повертає найбільше значення в ітерабельному об'єкті.
# sorted(iterable, *, key=None, reverse=False) Повертає новий відсортований список з елементів iterable.
#
# ### **Функції введення-виведення**
#
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) Друкує об'єкти до текстового потоку file, розділяючи їх sep та закінчуючи end.
# input([prompt]) Дозволяє користувачу ввести рядок тексту.
#
# ### **Приведення типів**
#
# int(x=0) Перетворює x в ціле число.
# float(x) Перетворює x в число з плаваючою точкою.
# str(x) Перетворює об'єкт x в рядок.
#
# ### **Інші вбудовані функції**
#
# type(object) Повертає тип об'єкта.
# id(object) Повертає "ідентифікатор" об'єкта, який є унікальним і незмінним для об'єкта протягом його життя.
# eval(expression, globals=None, locals=None) Виконує рядковий вираз expression і повертає результат.
# exec(object[, globals[, locals]]) Виконує програмний код Python, збережений у рядку або файлі.



# ### **Функції для роботи з ітерабельними об'єктами**
#
# all(iterable) Повертає True, якщо всі елементи ітерабельного об'єкта є істинними (або якщо ітерабельний об'єкт порожній).
# any(iterable) Повертає True, якщо хоча б один елемент ітерабельного об'єкта є істинним.
# filter(function, iterable) Використовує function для фільтрації елементів iterable, повертаючи ті, для яких function повертає True.
# map(function, iterable, ...) Застосовує function до кожного елементу iterable і повертає новий ітератор з результатами.
# range(start, stop[, step]) Генерує послідовність чисел від start до stop з кроком step.
# zip(*iterables) Створює ітератор, який агрегує елементи з кожного з ітерабельних об'єктів.



# list_with_args_negative = [True, False, 1, 0, '']
# list_with_args_positive = [True, 1, 'str']
#
# print(all(list_with_args_negative))
# print(any(list_with_args_negative))
# print()
# print(all(list_with_args_positive))
# print(any(list_with_args_positive))
#
# list_with_args_1 = [False, 0, '']
#
# print(all(list_with_args_1))
# print(any(list_with_args_1))

# zip(*iterables) Створює ітератор, який агрегує елементи з кожного з ітерабельних об'єктів.

# list_1 = [1, 2, 3, 4]
# list_2 = ['one', 'two', 'three']
# list_3 = [True, False, True]

# stat = [1, 10, 2000]
# name = ['kills', 'ratio', 'killed']
#
# res = dict(zip(name, stat))
#
# assert 1 == res.get('kills')
# result = zip(list_1, list_2)


# for item in result:
#     print(item)



# result = map(lambda x: x ** 2, [1, 2, 3, 4])

# for item in result:
#     print(item)

# def click_on():
#     pass
#
# def execute(func):
#     func()
#
#
#
# flow_a = [click_on, click_on, click_on] # flow a
# [click_on, click_on, click_on, click_on, click_on] # flow b
#
# map(lambda func: func(), flow_a)

# def click_on(place_to_click):
#     pass
#
# places_to_click = ['title', 'button', 'drop-down']
#
#
# map(click_on, places_to_click)
#
# click_on('title')
# click_on('button')
# click_on('drop-down')


# ### **Функції для роботи з колекціями**
#
# len(s) Повертає кількість елементів у об'єкті.
# min(iterable, *[, default=obj, key=func]) Повертає найменше значення в ітерабельному об'єкті.
# max(iterable, *[, default=obj, key=func]) Повертає найбільше значення в ітерабельному об'єкті.
# sorted(iterable, *, key=None, reverse=False) Повертає новий відсортований список з елементів iterable.



# print(len([1, 2, 3, 4]))
# print(len('qwertyu'))

# print(min([1, 2, 3, 4, 5]))
# print(min(['asd', 'daswqe', 'asdwqfsad', 'asdwqasd']))

# print(max([1, 2, 3, 4, 5]))


# print(sorted([123, 13, 632, 123, 546, 231], reverse=True))
# print(sorted(['asd', 'daswqe', 'asdwqfsad', 'asdwqasd'], reverse=False))


# type(object) Повертає тип об'єкта.
# id(object) Повертає "ідентифікатор" об'єкта, який є унікальним і незмінним для об'єкта протягом його життя.
# eval(expression, globals=None, locals=None) Виконує рядковий вираз expression і повертає результат.
# exec(object[, globals[, locals]]) Виконує програмний код Python, збережений у рядку або файлі.


# print(type(10))
# print(type(10.))
# print(type('asd'))
# result = type(10)
#
# print(result is int)

# def instance(arg, t):
#     return type(arg) is t
#
#
# print(instance(10, int))
# print(instance(10, str))
# print(isinstance(10, str))



# result = eval('isinstance(10, str)')
#
# print(result)

import json

# json.loads('{"key": "value"}')


# res = eval("{'key': 'value'}")
# print(res)
# print(type(res))


# ### **Функції для роботи з числами**

# absolute = abs(-10)
# print(absolute)
# print(-10)
#
# div = divmod(10, 2)
# print(div)
# print(10 % 2)
# print(10 // 2)


# res = pow(10, 2)
# print(res)
#
# number = 10.2124123123
# print(round(number, 2))
#
# list_with_args = [True, False, 1, 0, '']
# print(all(list_with_args))
# print(any(list_with_args))

# res = range(1, 10)
#
# for i in res:
#     print(i)
#
# list_1 = [1, 2, 3, 4]
# list_2 = ['one', 'two', 'three']
# list_3 = [True, False, True]
#
# result = zip(list_1, list_2)
#
# for item in result:
#     print(item)
#
#
# print(dict(result))

# result = map(lambda x: x ** 2, [1, 2, 3, 4])
#
# for item in result:
#     print(item)

# def click_on():
#     pass
#
# # [click_on, click_on, click_on] #a
# # [click_on, click_on, click_on, click_on, click_on] #b
# #
# # map()
#
# ['title', 'button', 'drop-down']
#
# map(click_on, places_to_click)


