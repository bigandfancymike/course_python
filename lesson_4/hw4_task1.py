# task1 Існує список з іменами ["john", "marta", "james", "amanda", "marianna"], перетворити рядок, щоб кожне ім'я явно починалися з великої літери.

list1 = ["john", "marta", "james", "amanda", "marianna"]

updated_names = [name.capitalize() for name in list1]

print(updated_names)