# Модифікувати попередню програму так, щоб вона також обробляла помилку введення, коли введене значення не може бути перетворене
# на число (ValueError), виводячи користувачеві зрозуміле повідомлення про помилку. (потрібно написати ще одну програму

import math

class NegativeNumberError(Exception):

    def __init__(self, number):
        self.number = number
        super().__init__(f"Корінь з від'ємного числа не визначений: {number}")

try:
    number = input("Введіть число: ")
    if not number.replace('.', '').isdigit():
        raise ValueError
    number = float(number)
    if number < 0:
        raise NegativeNumberError(number)
    else:
        square_root = math.sqrt(number)
        print(f"Квадратний корінь з {number} = {square_root}")
except ValueError:
    print("Ви ввели некоректне число.")
except NegativeNumberError as e:
    print(e)
finally:
    print("Завершення операції обчислення")

