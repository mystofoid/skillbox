# Задача 2. Игра
# Вам предстоит создать 2D-игру (вид сверху, игрок двигается в двух плоскостях).

# Начнём с управления персонажем: получаем от игрока пройденное расстояние и угол, по которому двигался персонаж. Зная эту информацию, нужно изменить текущие координаты (0, 0) на новые (х, у). Чтобы это сделать, требуется узнать, какое расстояние персонаж преодолеет по горизонтали (по оси Х, x = расстояние × косинус угла) и по вертикали (по оси У, y = расстояние × синус угла).

# Напишите программу, которая получает на вход расстояние и угол поворота. Выведите координаты нового местоположения персонажа.

import math

# angle = float(input('Введите угол положения в градусах: '))
# distance = float(input('Введите расстояние до танка: '))

# angle /= 57.29577951308 # перевели градусы в радианы т.к. функция ждет их

# x = math.cos(angle) * distance
# y = math.sin(angle) * distance

# print(f'Координаты вражеского танка x = {x}, y = {y}')


distance = float(input("Пройденное расстояние: "))

# Ввод угла
# функции cos/sin принимают на вход радианы, значит нужно сделать перевод, сделать это можно по-разному:

# Вариант 1:
# angle = float(input("Угол поворота: "))
# angle /= 57.2958

# Вариант 2:

angle = math.radians(float(input("Угол поворота: ")))

x_coord = distance * math.cos(angle)
y_coord = distance * math.sin(angle)

print("Координаты нового местоположения - (", x_coord, ",", y_coord, ")")