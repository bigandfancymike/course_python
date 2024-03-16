#Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно.
# Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями.
def sum_range(start, end):
    # Перевірка чи потрібно поміняти місця чисел
    if start > end:
        start, end = end, start

    total = 0
    for num in range(start, end + 1):
        total += num

    return total

start = 3
end = 1
print("Сума чисел від", start, "до", end, "включно:", sum_range(start, end))

