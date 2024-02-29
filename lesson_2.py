# str
import sys

my_string = 'my_string'
my_string_2 = str()

print(my_string)
print(my_string_2, 'string1', end='***')

# int
integer = 10
integer_1 = int()
print(integer)
print(integer_1)

# float
floating = 10.000000000
floating_1 = float()

# list
list_1 = [1, 2, 3]
list_2 = list()

print(id(list_1))

list_1.append('new_value')

print(list_1)
print(id(list_1))

# tuple

tuple_1 = (1, 2, 3)
tuple_2 = tuple()

print(tuple_1)
print(tuple_2)

# dict словники
dictionary = {10: 80, 'city': 'Kyiv'}
dictionary_1 = dict()

print(id(dictionary))

dictionary['country'] = 'Ukraine'
print(id(dictionary))

print(dictionary)
#print(dictionary_1)

# set - множини, котрі у собі мають унікальні значення
#set_1 = {1, 2, 3}
#set_2 = set()
#set_2 = set([1, 2, 3])

#set_1.add(3)
set_1 = {'a', 'r', 'y'}

print(set_1)
#print(set_2)

# frozenset
frozenset_1 = frozenset([1, 2, 3, 4])

# bool
am_i_human = True
am_i_dog = False

is_true = 1
is_false = 0

is_true_1 = 'sting'
is_false_1 = ""

#
# # mutable
# list
# set
# dict
#
# # immutable
# int
# str
# float
# tuple
#
# # ordered/упорядковані
# set
# list
# tuple
# str

# unordered
# set

#import_sys
l = [1, 2, 3]
t = (1, 2, 3)

print('list', sys.getsizeof(l), sep='=')
print('tuple', sys.getsizeof(l), sep='=')
