'''
Задача 1. Степень нечётного числа

Выведите третью степень каждого нечётного числа в диапазоне от единицы до указанного
'''
n = int(input('Введите число: '))
for number in range(1, n + 1, 2):
  print(number, '** 3 =', number ** 3)
