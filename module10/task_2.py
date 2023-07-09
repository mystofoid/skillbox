# Задание 2. Лестница
# Что нужно сделать
# Напишите программу, которая выводит «лестницу» из чисел, когда пользователь вводит число N:

size = int(input('Введите число: '))
count = 0
for row in range(1, size + 1,):
    for col in range(row):
        print(row, end=' ')
    print()