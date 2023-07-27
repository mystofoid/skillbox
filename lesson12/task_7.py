# Задача 1. Среднее арифметическое
# Программа получает от пользователя два числа — a и b. Реализуйте функцию, которая принимает на вход числа a и b, считает и выводит в консоль среднее арифметическое всех чисел из отрезка [a; b]. Обеспечьте контроль ввода: не забывайте, что а всегда должно быть меньше, чем b.

 

# Пример:

# Введите левую границу: 3

# Введите правую границу: 8

# Среднее: 5.5


# Усложнение: сделайте это без использования циклов.

# 1
# def calcTool(x, y):
#     sumNumbers, countNumbers = 0, 0
#     for i in range(x, y + 1):
#         sumNumbers += i
#         countNumbers += 1
#     print(f'Сраднее: {round(sumNumbers / countNumbers, 2)}')

# 2
# def calcTool(x, y): # Без Цикла
#     print(f'Среднее: {round((x + y) / 2, 2)}')

# a = int(input('Введите a: '))
# b = int(input('Введите b: '))

# if a > b:
#     a, b = b, a

# calcTool(a, b)

# 3

def calcTool(x, y):
    list_num = list(range(a, b + 1))
    average = sum(list_num) / len(list_num)
    print(f'Среднее: {average, list_num}')



a = int(input('Введите a: '))
b = int(input('Введите b: '))

if a > b:
    a, b = b, a

calcTool(a, b)