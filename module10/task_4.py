print('Задача 4. Крест')

# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)




# ^        ^
#  ^      ^
#   ^    ^
#    ^  ^
#     ^^
#     ^^
#    ^  ^
#   ^    ^
#  ^      ^
# ^        ^

breadth = int(input('Введите значение ширины: '))
height = breadth * 2

for row in range(breadth):
  for col in range(height):
    if col == row:
      print('^', end= '')
    elif col == -row + breadth - 1:
      print('^', end= '')
    else:
      print(' ', end= '')
  print()
