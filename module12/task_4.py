# Задача 4. Число наоборот
# Что нужно сделать
# Вводится последовательность чисел, оканчивающаяся нулём. Реализуйте функцию, которая принимает в качестве аргумента каждое число, переворачивает его и выводит на экран.

# Пример:

# Введите число: 1234
# Число наоборот: 4321
# Введите число: 1000
# Число наоборот: 0001
# Введите число: 0
# Программа завершена!

# Дополнительно: добейтесь такого вывода чисел, в начале которых идут нули.

# Пример:

# Введите число: 1230
# Число наоборот: 321

# Ноль, который мы убрали, называется ведущим.

def contrary(number):
    while True:
        cycle = 0
        if number != 0:
            print('Число наоборот: ', end='')
            while number > 0:
                cycle += 1
                temp = number % 10
                number //= 10
                if temp == 0 and cycle == 1:
                    cycle = 0
                    continue
                print(temp, end='')
            print()
        else:
            print('Программа завершена!')
            break
        number = int(input('Введите число: '))

number = int(input('Введите число: '))
contrary(number)
