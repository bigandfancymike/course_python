# task2 Користувач вводить текст і слово, яке потрібно знайти, якщо це слово є в тексті, вивести 'YES', інакше 'NO'


text = input('Текст користувача: ')
word_to_look = input('Слово користувача: ')


if word_to_look in text:
    print('YES')
else:
    print('NO')


