print('Задача 3. Апгрейд калькулятора')

# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
#
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
#
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
#
# Напишите программу,
# которая спрашивает у пользователя число и действие,
# которое нужно с ним сделать:
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру.
#
# Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.

def summa_n(n):
  temp = n
  summ = 0
  while temp != 0:
    summ += temp % 10
    temp //= 10
  print(f"\nСумма цифр в последовательности {n} равна {summ}")
  print()

def max_num(n):
  number = n
  num = 0
  number_max = 0
  while n > 0:
    num = n % 10
    n //= 10
    if num > number_max:
      number_max = num
    else:
      num = 0
  print(f"\nМаксимальная цифра в последовательности {number} равна {number_max}")
  print()

def min_num(n):
  number = n
  number_min = n % 10
  while n > 0:
    if n % 10 <= number_min:
      number_min = n % 10
      n = n // 10
    else:
      n = n // 10
  print(f"\nМинимальная цифра в последовательности {number} равна {number_min}")
  print()

def main_menu():

  while True:
    try:
      n = int(input("Введите любое целое число: "))
      break
    except ValueError:
      print("Ошибка ввода. Вы ввели не целое число. Повторите ввод.")

  while True:
    try:
      choice = int(input("Введите цифру 1 - если надо вывести сумму цифр числа.\nВведите цифру 2 - если надо вывести максимальную цифру из введенного числа.\nВведите цифру 3 - если надо вывести минимальную цифру из введенного числа.\nВведите цифру 1, 2 или 3: "))
      if choice == 1:
        summa_n(n)
      elif choice == 2:
        max_num(n)
      elif choice == 3:
        min_num(n)
      else:
        print("Ошибка ввода.")
      break
    except ValueError:
      print("Вы ввели не целое число или не число. Повторите ввод.")
    main_menu()

main_menu()
