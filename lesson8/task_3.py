'''
Задача 3. Квадраты нечётных чисел

Вводится число N. Напишите программу, которая выводит квадраты нечетных чисел от 1 до N.
Нельзя использовать условные операторы. Можно использовать цикл while, но постарайтесь всё-таки решить с
помощью конструкции for in range. Не нужно искать решение в интернете, попробуйте подумать сами, в следующем
уроке мы обязательно разберём эту задачу.

n = int(input('Введите число N: '))
for number in range(1, n // 2 + n % 2 + 1):
    number = number * 2 - 1 #определение нечетного числа
    print(number, '** 2 =', number ** 2)
'''
n = int(input('Введите число N: '))
for number in range(1, n + 1, 2): # 1 - start, n - stop, 2 - step, шаг в range решает это выражение range(1, n // 2 + n % 2 + 1)
    print(number, '** 2 =', number ** 2)

