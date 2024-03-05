# task 1 - transfer temperature from celsius to fahrenheit and kelvin

celsius = float(input('Введіть температуру в целсіях: '))
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15

print(f'Результат температури по Фаренгейту: {fahrenheit} °F') # з цим допоміг chatgpt - не дуже розумію, насправді що таке f в цьому рядку
print(f'Результат температури в Кельвінах: {kelvin} °K')