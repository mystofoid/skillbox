'''
Задача 3. Прятки 2

Пока все прятались, “голя” решил схитрить и считать секунды быстрее, чем нужно.

Напишите программу, которая выводит только чётные числа в порядке убывания от N до 1 включительно, используя цикл for. Нельзя использовать условный оператор.
'''
seconds = int(input('Введите кол-во секунд: '))
for second in range(seconds, 0, -2):
  print(second)
print('Я иду искать!')
