print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

seqNum = int(input('Сколько чисел будем вводить: '))
maxs = 0
for count in range (1, seqNum + 1):
  numbers = int(input(f'Введите {count}-е число: '))
  temp = numbers
  summ = 0
  while temp > 0:
    summ += temp % 10
    temp //= 10
  if summ > maxs:
    maxs = summ
    maxNumber = numbers
print(f'Максимальная сумма цифр = {maxs} у числа {maxNumber}')
