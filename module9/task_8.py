print('Задача 8. Колонтитул')

# Нам нужно написать программу для печати важных объявлений.
# Сверху объявления должен располагаться вот такой колонтитул:
#  ~~~~~~~~~~!!!!!!~~~~~~~~~~
# Восклицательные знаки всегда располагаются по центру строки,
# причём в зависимости от важности объявления количество восклицательных знаков может быть разным.
#
# Напишите программу,
# которая спрашивает у пользователя сначала общую длину колонтитула в символах,
# потом желаемое количество восклицательных знаков,
# после чего выводит на экран готовую строку.

length = int(input('Введите длину колонтитула в символах: '))
pling = int(input('Введите кол-во восклицательных знаков: '))
halfLenght = (length - pling) // 2

print('\n')
for symbol in range(halfLenght):
  print('~', end='')
for symbol in range(pling):
  print('!', end='')
for symbol in range(halfLenght):
  print('~', end='')
print('\n')

