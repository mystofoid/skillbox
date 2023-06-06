# Задача 5. Отрезок
# Что нужно сделать
# Напишите программу, которая считывает с клавиатуры два числа: a и b, — считает и выводит в
# консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3.
start = int(input('Введите начало отрезка: '))
stop = int(input('Введите конец отрезка: '))
summ= 0
count = 0
for i in range(start, stop + 1):
    if i % 3 == 0:
        # print('i', i)
        summ += i
        print('summ', summ)
        count += 1
        print('count', count)
midle = summ / count
print(midle)