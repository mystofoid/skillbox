print('Задача 1. Урок информатики 2')


# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
#
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
#
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
#
# Пример 1:
#
# Введитечисло: 92345
#
# Формат плавающей точки: x = 9.2345 * 10 ** 4
#
# Пример 2:
#
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3

def exp_num_2(x):

  while x <= 0:
    x = float(input("Введите число больше 0: "))
  x_1 = x

  cycle = 0
  cycle_1 = 0
  devider = 1
  devider_1 = 1

  if x < 1 and x > 0:

    while x <= 1:
      cycle_1 += 1
      x *= 10
    for i in range(cycle_1):
      devider_1 *= 10
    # print(devider_1)
    fraction = x_1 * devider_1
    verification = fraction * 10 ** (- cycle_1)
    print(f"Число {verification} в формате плавающей точки \nвыглядит так: x = {fraction} * 10 ** {-cycle_1}")

  else:

    while x > 9:
      cycle += 1
      x //= 10

    for i in range(cycle):
      devider *= 10
    # print(devider)

    fraction = x_1 / devider
    verification = fraction * 10 ** (cycle)
    print(f"Число {verification} в формате плавающей точки \nвыглядит так: x = {fraction} * 10 ** {cycle}")

x = float(input("Введите число: "))
exp_num_2(x)
