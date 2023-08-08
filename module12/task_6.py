# Задача 6. НОД
# Что нужно сделать
# Напишите функцию, вычисляющую наибольший общий делитель двух чисел.

def calc_largest_devider():
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    num_1 = number_1
    num_2 = number_2
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    print(f'НОД чисел {num_1} и {num_2} равен', number_1 + number_2, number_1, number_2)

calc_largest_devider()
