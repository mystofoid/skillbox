# Задача 4. Площадь треугольника
# Что нужно сделать

# Напишите программу, которая запрашивает у пользователя длины двух катетов в прямоугольном треугольнике и выводит его площадь.
# S = ab / 2
# Советы и рекомендации

# Не стоит применять целочисленное деление, это не совсем корректно.
# Обратите внимание на написание переменной S: её нужно писать как s, со строчной.


# Что оценивается

# Вычисления корректны, применены правильные операции.
# В input содержится корректное приглашение для ввода.
# Есть пробелы после запятых и при бинарных операциях.

a = int(input('Введите длинну стороны "a" в треугольнике: '))
b = int(input('Введите длинну стороны "b" в треугольнике: '))
s = (a * b) / 2
print('Площадь прямоуголного треугольника равна ', s, 'квадратных мм' )
