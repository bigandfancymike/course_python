# # #1 Повторне використання - основна перевага у роботі з функціями
# #
# # # def say_hi():
# # #     print('Hi, there!')
# # #
# # # say_hi()
# #
# # list_numbers = [1, 2, 3]
# # list_words = ['march', '2024', 'python']
# #
# # # for number in list_numbers:
# # #     print(number)
# # #
# # # for words in list_words:
# # #     print(word)
# #
# # def iter_through_list(l):  #l = list
# #     for item in l:
# #         print(item)
# # #
# # # iter_through_list(list_numbers)
# # #
# # # iter_through_list(list_words)
# #
# # # def plus(a, b):
# # #     print(a + b)
# # #
# # # plus(10, 2 )
# #
# # for number in list_numbers:
# #     print(number)
# #
# # for word in list_words:
# #     print(word)
# #
# # iter_through_list(list_numbers)
# #
# # iter_through_list(list_words)
# #
# #
# # def click_on_login_button():
# #     pass
# #
#
# # def say_hello():
# #     print('hello, anya!')
# #
# # say_hello()
#
# # def say_hello(name):
# #
# #     print(f"Hello, {name}!")
# #
# # names = ('Anya', 'Kostya', 'Nazar')
# # for name in names:
# #     say_hello(name)
#
# list_1 = []
#
# # def plus(a, b):
# #     result = a + b
# #     return result
#
# # print(list_1.append(1))
# # result = plus(10, 5)
# #
# # print(result)
#
#
# # Scope
#
# my_favourite_game = 'golf'
# my_var = 10
#
# def print_favourite_game():
#
#     global my_favourite_game   #я хочу мати доступ до змінної my_favorite_game з глобального скоупу
#
#     print(my_favourite_game, 'My favourite game from func before new assign')
#
#     my_favourite_game = 'football'
#
#     print(my_favourite_game, 'My favourite game from func after new assign')
#
# # def print_favourite_game():
# #
# #     print(my_favourite_game, 'My favourite game out func')# # #1 Повторне використання - основна перевага у роботі з функціями
# # #
# # # # def say_hi():
# # # #     print('Hi, there!')
# # # #
# # # # say_hi()
# # #
# # # list_numbers = [1, 2, 3]
# # # list_words = ['march', '2024', 'python']
# # #
# # # # for number in list_numbers:
# # # #     print(number)
# # # #
# # # # for words in list_words:
# # # #     print(word)
# # #
# # # def iter_through_list(l):  #l = list
# # #     for item in l:
# # #         print(item)
# # # #
# # # # iter_through_list(list_numbers)
# # # #
# # # # iter_through_list(list_words)
# # #
# # # # def plus(a, b):
# # # #     print(a + b)
# # # #
# # # # plus(10, 2 )
# # #
# # # for number in list_numbers:
# # #     print(number)
# # #
# # # for word in list_words:
# # #     print(word)
# # #
# # # iter_through_list(list_numbers)
# # #
# # # iter_through_list(list_words)
# # #
# # #
# # # def click_on_login_button():
# # #     pass
# # #
# #
# # # def say_hello():
# # #     print('hello, anya!')
# # #
# # # say_hello()
# #
# # # def say_hello(name):
# # #
# # #     print(f"Hello, {name}!")
# # #
# # # names = ('Anya', 'Kostya', 'Nazar')
# # # for name in names:
# # #     say_hello(name)
# #
# # list_1 = []
# #
# # # def plus(a, b):
# # #     result = a + b
# # #     return result
# #
# # # print(list_1.append(1))
# # # result = plus(10, 5)
# # #
# # # print(result)
# #
# #
# # # Scoop
# #
# # my_favourite_game = 'golf'
# # my_var = 10
# #
# # def print_favourite_game():
# #
# #     global my_favourite_game   #я хочу мати доступ до змінної my_favorite_game з глобального скоупу
# #
# #     print(my_favourite_game, 'My favourite game from func before new assign')
# #
# #     my_favourite_game = 'football'
# #
# #     print(my_favourite_game, 'My favourite game from func after new assign')
# #
# # # def print_favourite_game():
# # #
# # #     print(my_favourite_game, 'My favourite game out func')

# def global_arg_plus_one():
#     global x
#     x += 1
#
# global_arg_plus_one()

# Non local scope

# def main():
#     name = 'Anya'
#
#     def inner():
#         print(name)
#
#     return inner
#
# func = main()
#
# func()

# def main():
#     var = 'from main'
# # db = connect_db(username_1) # admin
#     def inner():
#         nonlocal var
#             #db = connect_db(username_2)
#         var = 'from inner'
#         print(var)
#
#     #db.get_data()
#
#     inner()
#     print(var, 'main print')
#
# main()


# Aргументи функцій

# def iter_through_list(list_first_argument, list_second_argument):
#     list_first_argument.extend(list_second_argument)
#     for item in list_first_argument:
#         print(item)
#
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c', 'd']
#
# iter_through_list(list1, list2)
#
# def grant_access(age, is_admin):
#     if type(age) is not int:
#         raise ValueError(f'Type of age is not int {type(age)}')
#     if is_admin:
#         return True
#     elif age >= 18:
#         return True
#     else:
#         return False

# print(grant_access(False, 10))  #Failed
# print(grant_access(10, False)) #correct

# print(grant_access(is_admin=True, age=10))

# args & kwargs

# def iter_through_list(*args):
#     for item in args:
#         if isinstance(item, str):
#             print(item)
#
# list_1 = [1, 2, 3, 4, 5]
#
# iter_through_list('Anya', 2024, 3, 11, 'Christmas')

# def iter_through_list_with_kwargs(**kwargs):
#     for item in kwargs.values():
#         if isinstance(item, str):
#             print(item)
#
# iter_through_list_with_kwargs(name = "Anya", year = 2024, month = 3)

d = {'key':10 , 'key_2':20}

# def del_item_from_dict_and_return(dictionary: dict, key_to_delete: str = 'key') -> dict:
#     if key_to_delete == 'key':
#         print(1)
#     if dictionary.get(key_to_delete):
#         result = dictionary.get(key_to_delete)
#         del dictionary[key_to_delete]
#         return result
#     else:
#         return False
#
# print(del_item_from_dict_and_return(d))


if __name__ == '__main__':

from typing

