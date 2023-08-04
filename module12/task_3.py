# Задача 3. Апгрейд калькулятора
# Что нужно сделать
# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия. Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру. Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.

def summa_n(number):
    number_temp = number
    sum_n = 0
    temp = 0
    while number > 0:
        temp = number % 10
        sum_n += temp
        number //= 10
    print(f'Сумма цифр в числе {number_temp} равна {sum_n}')

def max_digit(number):
    number_temp = number
    temp = 0
    digit_max = 0
    while number > 0:
        temp = number % 10
        number //= 10
        if temp > digit_max:
            digit_max = temp
        else:
            temp = 0
    print(f'Максимальная цифра в числе {number_temp} равна {digit_max}')
    print()

def min_digit(number):
    temp = number
    digit_min = number % 10
    while number > 0:
        if number % 10 <= digit_min:
            digit_min = number % 10
            number //= 10
        else:
            number //= 10
    print(f'Минимальная цифра в числе {temp} равна {digit_min}')
    print()

def menu():
    number = int(input('Введите число: '))
    choice = int(input('Введите: \n1 для суммы цифр в числе. \n2 для вывода минимальной цифры в числе. \n3 для вывода максимальной цифры в числе. '))
    if choice == 1:
        summa_n(number)
    elif choice == 2:
        min_digit(number)
    elif choice == 3:
        max_digit(number)
    else:
        print('Ошибка ввода, повторите ввод.')
        menu()
menu()