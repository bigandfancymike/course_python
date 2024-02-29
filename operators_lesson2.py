# арифметичні

# +
# -
# *
# /
# // цілочислене
# % з остачею
# **

# x = 100
# y = 18
#
# print(x % y)

my_str = 'Monday'

your_str = 'February'

#print(my_str + ' ' + your_str)
#print(my_str - your_str)

# -= Присвоювання
# -+= Додавання з присвоюванням
# --= Віднімання з присвоюванням
# -*= Множення з присвоюванням

x = 100

#Оператори порівняння
# - == Рівно
# - != Не рівно
# - > більше ніж
# - < менше ніж
# - >= більше ніж або рівно
# - <= менше ніж або рівно

# Приклад працюючої програмки
# my_age = int(input('Enter your age: '))
#
# allow_enter = 18
# #my_current_age = 15
#
# if my_age >= allow_enter:
#     print('Enter allowed')
#
# elif my_age <= allow_enter:
#     print('Enter declined')
#
# else:
#     print('I do not know your age, enter is not allowed')


# if bool1:
#     print('im from if and it was True')
# elif 0:
#     print('im from ELIF and it was True')
# else:  #else юзаєм тоді, коли усі попередні вирази були невірними, тобто для дефолтного значення можем це юзати
#     print("im from ELSE and it was True")

# Логічні оператори - Logical operators
# - and Повертає True, якщо обидва вирази є істинними
# - or Повертає True, якщо хоча б один з виразів є істинним
# - not Повертає заперечення виразу


# age = 18
# childhood_age = 6

# if age > 10 and childhood_age == 6:
#     print('Allow enter')
#
# else:
#     print('Im from else')

# if age < 10 or childhood_age == 6:
#     print('Allow enter')
#
# else:
#     print('Im from else')

# if not False:
#     print('Allow enter')
#
# else:
#     print('Im from else')


# is
# is not

# l = ['Laptop', 'Monitor', 'Mouse']
#
# list_1 = l
#
# if l is list_1:
#     print('yes')
# else:
#     print('no')

# if l == ['Laptop', 'Monitor', 'Mouse']:
#     print('yes all the same')


#оператори членства

# in перевіряє чи є у цього упорядкованому обєкті це значення,  яке нам треба
# not in

# l = ['Laptop', 'Monitor', 'Mouse']
#
# x = 10
#
# if 'table' in l:
#     print("table not in l")
# elif "chair" in l:
#     print('chair not in l')
# elif "chair" not in l:
#     print('hello world')
# else:
#     print("nothing here")


# матч кейси

# x = 10
# match x:
#     case 9 | 10: #if/elif      тут | - or
#         print('yes x is equal to 10 OR 9')
#     case 15: #if/elif
#         print('yes x is equal to 15')
#     case _:
#         print('nothing from about')


# age = 60
# clothe_color = 'blue'
#
# match clothe_color:
#
#     case 'blue' if age in range(18, 60):   #99 - 18 in 0-98
#         print('please welcome')
#     case 'red':
#         print('nope')
#     case _:
#         print('get out from here')

# for index in range(5, 50, 5):
#     print(index)

is_in = 10 in range(20)
print(is_in)

if 10 in range(20):
    print('good')
else:
    print('bad')