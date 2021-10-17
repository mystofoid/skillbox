
# Задача 1. Сумма чисел 2
# Пользователь вводит число N. Напишите функцию summa_n, которая принимает одно целое положительное число N и находит сумму всех чисел от 1 до N включительно. Функция вызывается два раза: сначала от числа N, а затем от полученной суммы.
# Пример работы программы:

# Введите число: 5
# Сумма от 1 до 5 = 15
# Сумма от 1 до 15 = 120

def summa_n(number):
    summ = 0
    for i in range(1, number + 1):
        summ += i
    print(f"Сумма от 1 до {number} = {summ}")
    return summ

number = int(input("Введите число: "))

number_1 = summa_n(number)
number_2 = summa_n(number_1)

