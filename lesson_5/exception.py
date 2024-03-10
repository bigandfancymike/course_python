
# from selenium.webdriver.support import expected_conditions as EC


# exception - базовий клас для більшості вбудованих винятків

# Exception

# AttributeError - виникає, коли атрибут об*єкта не знайдено

# class Today:
#
#     hour = 19
#     pass
# print(Today.minute)
#
# print('Everything is working')

# string = 'string'
# string.new()

# IOError  - виникає при виникненні помилку вводу/виводу (тепер замінений на OSError)

# ImportError - виникає коли імпортований модуль не може бути знайдений

# from lesson_3 import str_methods

# IndexError - виникає при спробі доступу до індексу за межами списку

# l = [1, 2, 3]
# print(l[3])

# KeyError - виникає, при спробі доступу до ключі словника, який не існує

# d = {'key': 'value'}
#
# # print(d['key_2'])
# print(d.get('key_2', 'такого ключа не існує'))

# NameError - виникає, коли локальна або глобальне ім*я не знайдено

# our_variable = 1
#
# print(our_variable_second)

# SyntaxError - виникає, коли інтерпретатор зіткнувся з синтаксичною помилкою

# counter = 0
# while counter <10:
#     print(1)
#     counter += 1

# ZeroDivisionError - виникає при спробі ділення на нуль

# x = 10 / 0

# TypeError - виникає при спробі операції з об*єктом неправильного типу

# print('10' + 10)

# print ('10' in 20)

# ValueError - виникає, коли функція отримує аргумент правильного типу, але з неприпустимим значенням

# print('Hello!'.index('q'))

# def my_func():
#     print(10)

# x = 10
#
# try: # у блоці try виконуємо якийсь код, що може видати нам помилку і  програма завершиться/ аби  програма не
#     # закінчувалась тоді, коли ми цього не очікуємо
#     result = 'Hello!'.index('l')
#     result1 = 'Hello!'.index('h')
#     result2 = 'Hello!'.index('oo')
#     result3 = 'Hello!'.index('qdasd')
#     result4 = 'Hello!'.index('qasdasd')
#     result5 = 'Hello!'.index('q')
#
# except KeyError:
#     print('Error just happened')

# x = 10
#
# try:
#     # 'Hello'.index('q')
#     d = {'key': 'value'}
#     res = d['key2']
# except ValueError as error:
#     print('Value error just happened')
# except KeyError as error:
#     print(f'Key error happened {error.__repr__()}')
# else:
#     print('Everything was ok')
# finally:
#     print('from finally')
# def make_some_changes_with_db():
#     try:
#         print('connect to DB')
#         print('Execute db command')
# # db_connection = SQLite(username, pwd) connect to DB
# # db_connection.flush()
#         'hello'.index('q')
#     except ValueError as error:
#         print(f'ValueError happened {error}')
#         return 0
#     return 1
# counter = 0
# counter += make_some_changes_with_db()
# counter += make_some_changes_with_db()
#
# print(f'{counter} connections are still open to DB')
# # except KeyError as error:
# #     print(f'KeyError happened {error.__repr__()}')
# # finally:
# print('Close connection to DB')

# class NikitaForgotValueErrorExampleException(Exception):
#     pass
#
# class NikitaForgotValueErrorExampleAssertion(AssertionError):
#     pass


# try:
#
#     d = {1: 2}
#     d[2] #буде помилка
#
#     #print('after exception') цей код вже не буде виконуватись через помилку вище
# except Exception as error:
#     print(error.__repr__())


    # raise NikitaForgotValueErrorExampleException('07 - missed value error')


# try:
#     result = 10/0
# except ZeroDivisionError as error:
#     print('Print do not divide by zero')
#
# print('Thanks for using our calculator')
#
# try:
#     result = 10 / 0
# except KeyError:
#     print('Print do not divide by zero')
# except Exception as error:
#     print(error)
#
# finally:
#     print('Thanks for using our calculator')
#
# print('im out from try')
#
#
# def func1():
#     pass
#
# def func2():
#     raise ZeroDivisionError
#
# def main():
#     func1()
#     func2()
#
# if __name__ == '__main__':
#     try:
#         main()
#     except KeyError as e:
#         pass
#     finally:
#         pass
