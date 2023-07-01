# Задача 3. Координатные оси
# Напишите программу, которая рисует координатные оси на поле 20×50. Результат должен получиться таким:

#                         |
#                         |
#                         |
#                         |
#                         |
#                         |
#                         |
#                         |
#                         |
# ---------------------------------------------------
#                         |
#                         |
#                         |
#                         |
#                         |
#                         |
#                         |
#                         |
#                         |
#                         |
#                         |
# Что нужно поменять в коде, что в середине был не дефис, а вертикальная палочка?

# row_size = 20
# col_size = 50
# for row in range(row_size + 1):
#     for col in range(col_size + 1):
#         if row == 9 and col == 24: # для того чтобы в центре был дефис
#             print('|', end='')
#         elif row == 9:
#             print('-', end='')
#         elif col == 24:
#             print('|', end='')
#         else:
#             print(' ', end='')
#     print()

row_size = 20
col_size = 50
for row in range(row_size + 1):
    for col in range(col_size + 1):
        if col == col_size // 2: # вначале нужно проверить на дефис, тогда и в центре будет дефис
            print('|', end='')
        elif row == row_size // 2:
            print('-', end='')
        else:
            print(' ', end='')
    print()