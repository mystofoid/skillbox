print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

height = int(input('Введите количество уровней пирамиды: '))
numeral = 1

for row in range(height):
  space = height - row - 1
  print('    ' * space, end = '')
  for col in range(row + 1):
      if numeral == 3 or numeral == 7:
          indent = 7
      elif numeral >= 9 and numeral < 101:
          indent = 6
      elif numeral >= 101 and numeral <= 109:
          indent = 5
      else:
          indent = 5
      print(numeral, end = ' ' * indent)
      numeral += 2
  print()
