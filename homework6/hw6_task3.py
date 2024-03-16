#Функція, яка приймає ввід від юзера з консолі та повертає введене значення, приклад вводу

def user_input():
    user_input = input("Введіть свої дані: ")
    return user_input

def print_data_type(data):
    try:
        data_type = type(eval(data)).__name__
        print("User is going to work with", data_type)
    except:
        print("Неможливо визначити тип даних")

user_data = user_input()

print_data_type(user_data)
