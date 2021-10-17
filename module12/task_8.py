print('Задача 8. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел



# 4  делитель      |4| 2 1
# 16 делитель 16 8 |4| 2 1

# divisor_a = []
# divisor_b = []

# for i in range(1, a + 1):
#   if a % i == 0:
#     divisor_a.append(i)
# for j in range(1, b + 1):
#   if b % j == 0:
#     divisor_b.append(j)
# print(divisor_a)
# print(divisor_b)

# Алгоритм нахождения НОД делением
# Большее число делим на меньшее.
# Если делится без остатка, то меньшее число и есть НОД (следует выйти из цикла).
# Если есть остаток, то большее число заменяем на остаток от деления.
# Переходим к пункту 1.
# Пример:
# Найти НОД для 30 и 18.
# 30 / 18 = 1 (остаток 12)
# 18 / 12 = 1 (остаток 6)
# 12 / 6 = 2 (остаток 0)
# Конец: НОД – это делитель 6.
# НОД (30, 18) = 6

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

def gcd(a, b):
  num_a = a
  nub_b = b
  while a != 0 and b != 0:
    if a > b:
      a = a % b
    else:
      b = b % a
  print(f"НОД чисел {num_a} и {nub_b} равен", a + b)

gcd(a, b)
