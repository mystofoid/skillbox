print('Задача 10. Яма ')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

depth = int(input('Введите глубину ямы: '))

for line in range(depth):
    for left_number in range(depth, depth - line - 1, -1):
        print(left_number, end="")
    point_count = 2 * (depth - line - 1)
    print("." * point_count, end="")
    for right_number in range(depth - line, depth + 1):
        print(right_number, end="")
    print()



# size = int(input('Введите размер матрицы: '))

# for row in range(size, 0, -1):
#   for leftcol in range(size, 0, - 1):
#     if leftcol >= row:
#       print(leftcol, end= '')
#     elif leftcol <= row:
#       print('.', end= '')
#   for rightcol in range(0, size + 1):
#     if rightcol >= row:
#       print(rightcol, end= '')
#     elif rightcol <= row - 2:
#       print('.', end= '')
#   print()
