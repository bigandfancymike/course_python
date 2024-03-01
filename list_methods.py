"""
- append(x) Додає елемент x`** в кінець списку.
- extend(iterable) Розширює список, додаючи в кінець всі елементи з ітерабельного об'єкта.
- insert(i, x) Вставляє елемент x`** на задану позицію i`**.
- remove(x) Видаляє перше входження елемента x`** зі списку. Якщо елемент не існує, генерується виняток ValueError`**.
- pop([i]) Видаляє елемент на позиції i`** і повертає його. Якщо індекс не вказано, видаляє та повертає останній елемент списку.
- clear() Видаляє всі елементи зі списку.
- index(x[, start[, end]]) Повертає індекс першого входження елемента x`** у списку (можна вказати діапазон пошуку).
- count(x) Повертає кількість входжень елемента x`** у списку.
- sort(key=None, reverse=False) Сортує елементи в списку на місці (аргументи key`** та reverse`** дозволяють кастомізувати сортування).
- reverse() Реверсує порядок елементів у списку на місці.
- copy() Повертає поверхневу копію списку.
"""

#
# list1 = [1, 2, 3, 566, 4]
#
# list2 = list1.copy()
# print(list1)
# print(list2)

# list2 = [5,6]
# #list1.extend(list2)
#
# #list1.insert(1, 'hello world')
#
# #list1.remove('hello world')
# # list1.clear()
# list1.sort(reverse=False)
# print(list1)

# #list1.append(5)
# list1.extend('hello')
# print(list1)





# list1 = [1, 2, 3, 3, 33, 1, 5, 6, 9,]
#
# list1.append(3)
#
# list2 = [3, 2, 1, 1]
# list1.extend(list2)
#
# list1.insert(2, 'new_item')
#
# list3 = list1.copy()

# print(list1)
# print(list2)
# print(list3)
#
#
#
#
# # Slicing
#
#
# list1 = [1, 2, 3, 3, 33, 1, 5, 6, 9]
#
#
# # print(list1[ 'початок'    : "кінець"  :  "шаг"   ])
#
# list2 = list1[::]
#
# print(list1)
# print(list2)
#
# # reverse
#
# print(list1[::-1])



list1 = [1, 2, 3, 4, 5, 33, 66, 77]

list2 =list1[::]
print(list2)