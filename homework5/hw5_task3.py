# Розширити роботу нашого калькулятора, додавши можливість користувачеві вводити числа до тих пір,
# поки він не вирішить вийти, вводячи певне ключове слово (наприклад, "вихід").
#
# Забезпечити коректну обробку введення для виходу з програми без виникнення помилок.
#
# Використовуйте try, except, else, finally для обробки можливих винятків.

# number1 = float(input('Введіть перше число: '))
# number2 = float(input('Введіть друге число: '))
#
# operation = input('Введіть арифметичну операцію (+, -, *, /): ')
#
# if operation == '+':
#     result = number1 + number2
# elif operation == '-':
#     result = number1 - number2
# elif operation == '*':
#     result = number1 * number2
# elif operation == '/':
#     if number2 == 0:
#         print('На нуль ділити неможливо')
#         result = None
#     else:
#         result = number1 / number2
# else:
#     print('Щось невалідне')
#     result = None
#
# if result is not None:
#      print(f'Результат: {result}')

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Введіть коректне число.")

def get_operation():
    while True:
        operation = input("Введіть арифметичну операцію (+, -, *, /), або 'вихід' для завершення: ")
        if operation in ('+', '-', '*', '/'):
            return operation
        elif operation == 'вихід':
            return None
        else:
            print("Введено некоректну операцію.")

while True:
    number1 = get_number('Введіть перше число: ')
    if number1 is None:
        break

    number2 = get_number('Введіть друге число: ')
    if number2 is None:
        break

    operation = get_operation()
    if operation is None:
        break

    try:
        if operation == '+':
            result = number1 + number2
        elif operation == '-':
            result = number1 - number2
        elif operation == '*':
            result = number1 * number2
        elif operation == '/':
            if number2 == 0:
                print('На нуль ділити неможливо')
                continue
            else:
                result = number1 / number2
        print(f'Результат: {result}')
    except Exception as error:
        print(f"Помилка обчислення: {error}")
    finally:
        print('Нова операція далі з нового рядку')

print("Програма завершена.")