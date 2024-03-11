#  Написати програму, яка запитує у користувача число і обчислює його квадратний корінь.
#
# Передбачити обробку винятку, який виникає при спробі обчислення квадратного кореня з від'ємного числа, і вивести відповідне повідомлення.
# (Тут потрібно додати перевірку на відʼємне число та якщо воно дійсно таке, то спонукати помилку за допомогою ключового слова raise, та створіть свою помилку котра будете спонукати)
#
# Використати else для виведення результату, якщо обчислення пройшло успішно.
#
# Додати конструкцію finally, яка виводитиме повідомлення про завершення операції обчислення.

# import math
#
# try:
#     number = float(input("Введіть число: "))
#     if number < 0:
#         print("Корінь з від'ємного числа не визначений.")
#     else:
#         square_root = math.sqrt(number)
#         print(f"Квадратний корінь з {number} = {square_root}")
# except ValueError:
#     print("Ви ввели некоректне число.")
# finally:
#     print("Завершення операції обчислення")


import math
class NegativeNumberError(Exception):

    def __init__(self, number):
        self.number = number
        super().__init__(f"Корінь з від'ємного числа не визначений: {number}")

try:
    number = float(input("Введіть число: "))
    if number < 0:
        raise NegativeNumberError(number)
    else:
        square_root = math.sqrt(number)
        print(f"Квадратний корінь з {number} = {square_root}")
except ValueError:
    print("Ви ввели некоректне число.")
except NegativeNumberError as error:
    print(error)
finally:
    print("Завершення операції обчислення")
