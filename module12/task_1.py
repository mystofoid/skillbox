# Задача 1. Сумма чисел
# Что нужно сделать
# Напишите функцию summa_n, которая принимает одно целое положительное число N и выводит сумму всех чисел от 1 до N включительно.

# Пример работы программы:

# Введите число: 5

# Я знаю, что сумма чисел от 1 до 5 равна 15



def summa_n(number):
    sum_n = 0
    for i in range(1, number + 1):
        sum_n += i
    print(f'Сумма чисел от 1 до {number} равна {sum_n}')

number = int(input('Введите число: '))
summa_n(number)