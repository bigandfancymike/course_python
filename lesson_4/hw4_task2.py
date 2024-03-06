# task2 - У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] , перетворити його у список змінних для Пайтона snace_case, "friends_list", "my_tuple"]

camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = [item[0].lower() + item[1:].replace('I', '_i').replace('L', '_l').replace('T', '_t').lower() for item in camel_case_list]
print(snake_case_list)



# l = ['NewCase']
# new_case = l[0][0].lower() + l [0][1:].replace('C', '_c')
# print(new_case)




