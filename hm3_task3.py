# task3 Валідатор для пошти, перевірка на символ '@' і '.', і якщо це так, вивести "YES", інакше "NO"

user_email = input('Введіть свою пошту: ')

if '@' in user_email and '.' in user_email:
    print('YES')
else:
    print('NO')