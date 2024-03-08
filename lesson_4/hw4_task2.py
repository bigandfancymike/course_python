# task2 - У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] , перетворити його у список змінних для Пайтона snace_case, "friends_list", "my_tuple"]

camel_case_list = ["FirstItem", "FriendsList", "MyTuple", "WonMatch"]
snake_case_list = []

for item in camel_case_list:
    snake_case_word = ""
    for i in range(len(item)):
        if item[i].isupper() and i != 0:
            snake_case_word += '_' + item[i].lower()
        else:
            snake_case_word += item[i].lower()
    snake_case_list.append(snake_case_word)
print(snake_case_list)



