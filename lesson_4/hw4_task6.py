# task 6
#  Напишіть програму котра підраховує кількість однакових символів у значенні котре введе користувач в консолі
# Приклад
# Користувач вводить abcdefgabc
# Очікуваний результат a,2 c,2 b,2 e,1 d,1 g,1 f,1
# Підказка: Використуйте dict для збереження пари key/value.
# Для виводу викоритуйте dict.get() метод з дефолтнім значенням для випадків коли ключа не існує .
# Використайте str.join() метод та dict comprehension для виводу результату

user_input = input('Введіть текст: ')

character_count = {}

for character in user_input:
    character_count[character] = character_count.get(character, 0) + 1

result = ", ".join(f"{char},{count}" for char, count in character_count.items())
print(result)

