# Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення :
# периметр квадрата, площа квадрата та діагональ квадрата. Надрукуйте їх

import math
def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    return perimeter, area, diagonal

side_length = 10
perimeter, area, diagonal = square(side_length)

print("Периметр квадрата:", perimeter)
print("Площа квадрата:", area)
print("Діагональ квадрата:", diagonal)

