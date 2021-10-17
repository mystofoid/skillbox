print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

def num_rev(num):
  num_reverse = ""
  while num != 0:
    num_temp = num % 10
    num //= 10
    num_reverse += str(num_temp)
  return num_reverse

for i in range(1, 2 + 1):
  if i == 1:
    num = int(input(f"Введите первое число: "))
    num_1_reverse = num_rev(num)
  else:
    num = int(input(f"Введите второе число: "))
    print()
summ = int(num_1_reverse) + int(num_rev(num))

print(f"Первое число наоборот: {num_1_reverse}")
print(f"Второе число наоборот: {num_rev(num)}")
print()

print("Сумма:", summ)
print(f"Сумма наоборот: {num_rev(num = summ)}")

# def reverse_num_summ(num_1, num_2):

#   num_1_temp = 0
#   num_2_temp = 0
#   summ_temp = 0
#   num_1_reverse = ""
#   num_2_reverse = ""
#   summ_reverse = ""

#   while num_1 != 0:
#     num_1_temp = num_1 % 10
#     num_1 //= 10
#     num_1_reverse += str(num_1_temp)
#   print("Первое число наоборот:", num_1_reverse)

#   while num_2 != 0:
#     num_2_temp = num_2 % 10
#     num_2 //= 10
#     num_2_reverse += str(num_2_temp)
#   print("Второе число наоборот:", num_2_reverse)
#   print()

#   summ = int(num_1_reverse) + int(num_2_reverse)
#   print("Сумма:", summ)

#   while summ != 0:
#     summ_temp = summ % 10
#     summ //= 10
#     summ_reverse += str(summ_temp)
#   print("Сумма наоборот:", summ_reverse)

# num_1 = int(input("Введите превое число: "))
# num_2 = int(input("Введите второе число: "))

# reverse_num_summ(num_1, num_2)
