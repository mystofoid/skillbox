# Задача 7. Режем число на части
# Что нужно сделать

# Реализуйте программу, которая получает на вход четырёхзначное число и выводит на экран каждую его цифру отдельно (в одну строчку либо каждую цифру в новой строчке). Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания. Однако можно использовать сколько угодно переменных.



# Что оценивается

# Результат вычислений корректен.
# В input содержится корректное приглашение для ввода.
# Есть пробелы после запятых и при бинарных операциях.

num = int(input('Введите 4-х значное число: '))
num_1 = num // 1000
num_2 = num // 100 % 10
num_3 = num // 10 % 10
num_4 = num % 10
print('', num_1, '\n', num_2, '\n', num_3, '\n', num_4)
