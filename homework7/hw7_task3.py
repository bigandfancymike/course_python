# Напишіть програму котра буде приймати назву функцій з консолі (input) (вони повинні існувати) та за допомогою
# built-in функції виводьте результат виконання переданої функції

# def main():
#     function_name = input("Введіть назву функції (наприклад, len): ")
#
#     if hasattr(__builtins__, function_name): #об*єкт, де шукаєм та сама функція
#         function = getattr(__builtins__, function_name)
#         result = function(input("Введіть аргумент (якшо потрібно): "))
#         print("Результат виклику функції:", result)
#     else:
#         print("Функція з назвою", function_name, "не існує.")
#
# if __name__ == "__main__":
#     main()


def main():
    function_name = input("Введіть назву функції (наприклад, len): ")

    if hasattr(__builtins__, function_name): #об*єкт, де шукаєм та сама функція
        function = getattr(__builtins__, function_name)
        argument = input("Введіть аргумент (якшо потрібно): ")
        result = function(argument)

        if result is not None:
            print("Результат виклику функції:", result)
        else:
            print("Функція", function_name, "повернула значення None.")
    else:
        print("Функція з назвою", function_name, "не існує.")

if __name__ == "__main__":
    main()