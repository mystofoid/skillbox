print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709


def series_sum(precision, x):

  start, i = 0, 0
  end, factorial, degree = 1, 1, 1
  while abs(end - start) > precision:
    start = end
    degree *= x * x
    i += 1
    factorial *= 2 * i * (2 * i - 1)
    if i % 2:
        end -= 1 * degree / factorial
    else:
        end += 1 * degree / factorial

  print(f'Сумма ряда = {end}')


precision = float(input('Введите точность: '))
x = int(input('Введите x: '))

series_sum(precision, x)
