# def annotation (arg):
#     if callable(arg):
#         print('Start program')
#         arg()
#         print('Finish')
#     else:
#         raise TypeError('Some error happened')
#
# def print_hi():
#     print('Hi')
#
# def triple(x: int):
#     return lambda y: x * y
#
#
# def check_if_callable(arg):
#     if callable(arg):
#         print('Start program')
#         print(arg(100))
#         print('Finish')
#     else:
#         raise TypeError('Some error happened')
#
# check_if_callable(triple(10))



# annotation(print_hi())


list_1 = [True, 0, False, 'str', '']
#
#
def func_1(x):
    return x % 2 == 0
#
# lambda_func = lambda x: x % 2

# print(lambda_func(11))
# print(func_1(11))

list_1 = [10 , 11, 20 , 23]


result = filter(lambda x: x % 2 == 0, list_1)
result_with_def = filter(func_1, list_1)


print(list(result), 'lambda')
print(list(result_with_def), 'def')


result = filter(lambda x: 'failed' in x, list_1)