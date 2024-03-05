# # [a, b, c, d]
# #  1  2  3  4
#
# # word
# # 1234
#
# dictionary_3 = {'date': 4, 'lesson_number': 'four', 10: 'int'}
#
# # for value in dictionary_3.values():
# #     print(value)
# #
# # for value in dictionary_3.keys():
# #     print(value)
# #
# # for key, value in dictionary_3.items():
# #     print('key', key)
# #     print('value', value)
#
# # list_of_elements = find_elements('locator')
# #
# # dictionary_elements = {'element_1': 'text', 'element_2': 'our word'}
#
# # for key, value in dictionary_elements.items():
# #     if value == 'our word':
# #         print(key)
#
# list_1 = ['anna', 'alyona', 'jerry']
# dictionary_1 = {}
#
# for index, value in enumerate(list_1):
#     dictionary_1[value] = index
#     # print('index', index)
#     # print('value', value)
#
# q = enumerate(list_1)
# print(next(q))
# print(next(q))
# print(next(q))
#
#
# print(dictionary_1)

# counter = 8
#
# while counter < 10:
#     print('Im from while')
#     counter += 1
#
# print('out from while')


# # boolean = True
#
# while boolean:
#     print('Im from while')
#     time.sleep(2)

# while True:
#
#     number_1 = int(input('number 1: '))
#     number_2 = int(input('number 2: '))
#     operator = input('operator: ')
#
#     if operator == '+':
#         print(number_1 + number_2)
#     elif operator == '/':
#         if number_2 == 0:
#             print('You entered wrong value')
#             continue
#         print('OK')
#
# counter = 0
# while counter <10:
#
#     if counter == 5:
#         continue
#     else:
#         print(counter)
#
#     counter += 1


# get data from DB
# string = ['my string', 'new', 'test data']
#
# for index, letter in enumerate(string):
#     if letter != 'new':
#         print(f'index of {letter} is {index}')
#     elif letter == 'test data':
#         break
#     string.pop()
#
# else:
#     print('db close()')


# counter = 0
#
# while counter <10:
#     print(counter)
#     counter += 1
#     if counter == 5:
#         break
#
# else:
#     print('I did not see break in while')


# LiST COMPREHENSION

#  [x+1     for x in range(5)    if  x%2 == 2]
# Do this   for this collection  In this situation

# l = [] - без лист комперехенш 4 рядки коду
#
# for i in range(10):
#     if i % 2 == 0:
#         l.append(i)
#
# print(l)

# з list comprehension

# l1 = [i for i in range(10) if i % 2 == 0]
#
# l2 = [True for i in range(10) if i %2 == 0]
#
# print(l1)
# print(l2)

#dict comprehansion

# {num: num*2 for num in range(5) if num%2 == 0}
#   do this   for this collection  in this situation

# d = {key: key / 10 for key in range(100, 120) if (key + 90) < 200}
#
# print(d)

#l1 = [i for i in range(10)]

new_str = ''.join([s for s in 'babasfasfasfasfasfasfqwre' if s.isupper()])
print(new_str)

