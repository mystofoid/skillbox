# Дана программа, которая запрашивает у пользователя два слова, а затем выводит их на экран два раза. Скопируйте эту программу в редактор и проверьте.

# a = input('Введите первое слово: ')
# b = input('Введите второе слово: ')
# print(a, b)
# # стереть эту строчку и вставить свой код здесь
# print(a, b)
# Задача: поменять значения переменных a и b местами. Изменять, удалять, менять местами первую, вторую, третью и последнюю строчки нельзя. Но в четвёртую строку можно вставлять сколько угодно кода, не трогая последний принт. Пример результата работы программы:

a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
a, b = b, a
print(a, b)
