# task7 - Перепишіть калькулятор з минулих дз, який буде продовжувати працювати при невірно введених даних юзером

# Додаткова умова: у юзера буде всього 2 спроби ввести правильні значення
# після другої спроби програма повинна завершуватись з повідомленням Спроби скінчились

given_attempts = 2

while given_attempts > 0:
    try:
        number1 = float(input('Введіть перше число: '))
        number2 = float(input('Введіть друге число: '))

        operation = input('Введіть арифметичну операцію (+, -, *, /): ')

        if operation in ['+', '-', '*', '/']:
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
            break
        else:
            if given_attempts == 2:  # Якщо це перша спроба, виведемо повідомлення
                print('Невірна операція, введіть арифметичну операцію (+, -, *, /):')
            given_attempts -= 1
    except ValueError:  #оцю штуку підгледів
        print('Неправильний формат. Остання спроба.')
        given_attempts -= 1

if given_attempts == 0:
    print('Спроби скінчились')
