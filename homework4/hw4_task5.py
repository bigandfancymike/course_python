# task5 - Дано лист types=[1, 1000, 2, 12, {'key': 'value'}
# Використовуючи break напишіть програму котра буде виводити тільки int тип даних, якщо тип буде інший зупинити цикл з повідомленням f'цикл не працює з {тут тип даних із-за якого ми зупинили цикл} типом даних'

types = [1, 1000, 2, 12, {'key': 'value'}]
for item in types:
    if type(item) is int:
        print(item)
    else:
        print(f'цикл не працює з {type(item)}')
        break