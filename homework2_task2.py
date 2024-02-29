# task 2 - program that will calculate the volume and temperature of the resulting mixture

v1 = float(input('Введіть перший об\'єм: '))
t1 = float(input('Введіть першу температуру: '))
v2 = float(input('Введіть другий об\'єм: '))
t2 = float(input('Введіть другу температуру: '))

volume = v1+v2
temperature = (v1 * t1 + v2 * t2) / (v1 + v2)

print(f'Результат об\'єму: {volume} літрів') #з цим допоміг chatgpt - не дуже розумію, насправді що таке f в цьому рядку
print(f'Результат температури: {temperature} С')