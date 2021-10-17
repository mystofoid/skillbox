print('Задача 8. Пирамидка')


# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######


height = int(input('Введите высоту пирамиды: '))

if height <= 0:
  print('Ошибка: высота елочки должна быть положительным числом.')
else:
  for line in range(height + 1):
    grid = 2 * line - 1
    space_count = height - line
    print(' ' * space_count, '#' * grid, sep='')

# width = height * 2
# grid = 1

# for i in range(1, width + 1, 2):
#   halfLenght = (width - i - grid) // 2
#   for symbol in range(halfLenght):
#     print(' ', end='')
#   for symbol in range(grid):
#     print('#' * i, end='')
#   for symbol in range(halfLenght):
#     print(' ', end='')
#   print()

