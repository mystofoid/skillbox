# Задача 2. Разминка для мозгов

# Напишите программу, которая проверяет то, как вы умеете складывать два числа в уме. Программа получает на вход два числа и предполагаемую сумму и должна выводить два разных сообщения — на верный и неверный ответ пользователя. В последнем случае надо показывать правильный результат.

# Пример:
# Введите первое число: 3
# Введите второе число: 10
# Сумма этих чисел: 13
# Ответ верный!

# Пример 2:
# Введите первое число: 3
# Введите второе число: 10
# Сумма этих чисел: 14
# Ответ неверный!

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
summ = num_1 + num_2
summ_hum = int(input('Какая сумма этих чисел? '))
if summ == summ_hum:
  print('Верно, сумма этих чисел: ', summ)
else:
  print('Неверно, ваш ответ: ', summ_hum)
