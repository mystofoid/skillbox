# Задача 3. Квадраты нечётных чисел
# Вводится число N. Напишите программу, которая выводит квадраты нечетных чисел от 1 до N. Нельзя
# использовать условные операторы. Можно использовать цикл while, но постарайтесь всё-таки решить
# с помощью конструкции for in range. Не нужно искать решение в интернете, попробуйте подумать
# сами, в следующем уроке мы обязательно разберём эту задачу.
#
number = int(input('Введите число: '))

'''for i in range(number // 2 + number % 2): # + number % 2 остаток от деления на 2 для нечетных
    # чисел (5 = 2 * 2 + 1) и (4 = 2 * 2 + 0)
    oddNum = i * 2 + 1
    print(oddNum, '** 2 =', oddNum ** 2)'''
for i in range(1, number + 1, 2):
    print(i, '** 2 =', i ** 2)