# Задача 1. Герон
# Существует, так называемая, формула Герона, позволяющая вычислить площадь треугольника, зная длины его сторон.

# S= √ (p * (p - a)*(p - b)*(p - c)), где

# S - площадь;
# p - полупериметр треугольника (a+b+c)/2;
# a,b,c - длины сторон треугольника.

# Напишите программу, которая принимает на вход длины сторон треугольника и выводит его площадь

import math

side_a = int(input('Введите длину стороны a в см.: '))
side_b = int(input('Введите длину стороны b в см.: '))
side_c = int(input('Введите длину стороны c в см.: '))


half_perimetr = (side_a + side_b + side_c) / 2
square_triangle = math.sqrt(half_perimetr * (half_perimetr - side_a) * (half_perimetr - side_b) * (half_perimetr - side_c))
print(f'Площадь треугольника равна {round(square_triangle, 2)} квадратных сантиметров.')

