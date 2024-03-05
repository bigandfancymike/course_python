# task 3 - basic calculator

number1 = float(input('Введіть перше число: '))  #тут або int або float, залежно від умови, але все-таки float більш валідно для калькулятора
number2 = float(input('Введіть друге число: '))

operation = input('Введіть арифметичну операцію (+, -, *, /): ')

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 == 0:
        print('На нуль ділити неможливо')
        result = None
    else:
        result = number1 / number2
else:
    print('Щось невалідне')
    result = None

if result is not None:
     print(f'Результат: {result}')   #з цим допоміг chatgpt - не дуже розумію, насправді що таке f в цьому рядку
