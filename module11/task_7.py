# Задача 7. За что?
# Что нужно сделать
# Вы встретились со старым другом, который тоже изучает программирование, но в другом учебном заведении. За чашкой кофе он пожаловался, что их сумасбродный препод дал задание написать программу, которая из двух введённых чисел определяет наибольшее, не используя при этом условные операторы, циклы и встроенные функции вроде max/min/sorted. Радуясь, что на вашем курсе такого не требуют, вы всё-таки решаете помочь другу. Напишите для него программу.

# Пример:

# Введите первое число: 10

# Введите второе число: 5

# Наибольшее число: 10

# Что оценивается
# Результат вывода соответствует условию.
# Input содержит корректное приглашение для ввода. 
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).
# Советы и рекомендации
# Рассмотрите разность суммы и разности чисел, сумму разности и суммы чисел.

# При необходимости можете использовать функцию abs(), позволяющую взять модуль числа.

a = int(input("Введите первое число: "))
b = int(input("Введите первое число: "))

print("Вариант № 1 Наибольшее число:", ((a + b) / 2 + abs(a - b) / 2))
print('Вариант № 2 Наибольшее число:', ((a + b + abs(a - b)) / 2))
print('Вариант № 3 Наибольшее число:', (a // b * a + b // a * b) // (a // b + b // a))