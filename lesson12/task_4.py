# Задача 1. Вода
# Одна бутылка воды «КлирВотер» от производителя «ВодЗавод» в разных магазинах стоит по-разному.

# Напишите программу, которая три раза вызывает функцию aboutWater, передаёт в неё один аргумент — цену на воду и выводит на экран название воды, производителя и цену.


# Пример:

# Название: КлирВотер
# Производитель: ВодЗавод
# Цена: 25


# Название: КлирВотер
# Производитель: ВодЗавод
# Цена: 30


# Название: КлирВотер
# Производитель: ВодЗавод
# Цена: 40

def aboutWater(price):
    print('\nНазвание: КлирВотер\nПроизводитель: ВодЗавод\nЦена:', price)
    print()

# aboutWater(25)
# aboutWater(30)
# aboutWater(40)

for _ in range(3):
    price = int(input('Введите цену воды: '))
    aboutWater(price)