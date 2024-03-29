# Задача 5. Вася хочет выигрывать
# Что нужно сделать
# Вася вдохновился фильмом «Двадцать одно» и решил изучить математику игровых автоматов. Для анализа данных ему нужна информация о том, как часто в автомате выпадает три или две одинаковых картинки.
# Для сбора данных нужна программа, проверяющая это равенство.
#
# Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадают) или 0 (если все числа разные).
#
# Советы и рекомендации
# По возможности уделите внимание сокращению кода. Избегайте проверки условий, которые уже проверены: если вы проверили условие condition, то не следует проверять not condition.
#
# Что оценивается
# input содержит корректное приглашение для ввода;
# в выводе может быть указано только число, но хорошим стилем считается описание вывода;
# правильное употребление пробелов после запятых при бинарных и логических операциях;
# правильно оформлены блоки if-elif-else, отступы одинаковы во всех блоках одного уровня.

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))
if num_1 == num_2 == num_3:
    print('Совпадает ', 3, 'числа')
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print('Совпадает ', 2, 'числа')
else:
    print('Совпадает ', 0, 'чисел')