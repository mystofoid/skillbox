print('Задача 2. Грубая математика')

# В одном аналитическом центре,
# где занимаются разного рода математическим анализом,
# работал практикант,
# который написал программу для расчёта некоторых функций.
# Правда, он в тот день очень устал
# и немного не так прочитал техническое задание
# и функции теперь рассчитываются довольно грубо.
#
# Вводится последовательность из N вещественных чисел.
# При этом положительные числа округляются вверх, отрицательные округляются вниз.
#
# Напишите программу,
# которая выводит натуральный логарифм от числа,
# если оно положительное, и экспоненту в степени числа, если оно отрицательное.
#
# Пример:
#
# Введите кол-во чисел: 3
# Введите число: 1.3
# x = 2   log(x) = 0.6931471805599453
#
# Введите число: -2.1
# x = -3   exp(x) = 0.049787068367863944
#
# Введите число: -5.9
# x = -6   exp(x) = 0.0024787521766663585

# !!! Не понял, что в итоге должно поучиться, точно или грубо? Сделал как в примере!!!

import math
num_sequence = int(input("Сколько чисел будем обрабатывать? "))

for i in range(1, num_sequence + 1):
  number = float(input(f"Введите {i}-е вещественное число: ")) #number = int(number + (0.5 if number > 0 else - 0.5)) если нужно округлить по матиматическим правилам
  if number > 0:
    # x = int(number + 0.5)
    x = math.ceil(number)
    # x = round(x, 1)
    x_log = math.log(x)
    print(f"x = {x}\tlog(x) = {x_log}")
  else:
    # x = int(number - 0.5)
    x = math.floor(number)
    # x = round(x, 1)
    x_exp = math.exp(x)
    print(f"x = {x}\texp(x) = {x_exp}")
  print()

