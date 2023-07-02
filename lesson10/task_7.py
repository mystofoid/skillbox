# Задача 1. Врата
# Напишите программу, которая выводит в консоль «врата», состоящие из тире, вертикальных линий и пробелов. Поле состоит из 20 строк и 30 столбцов (но не стесняйтесь пробовать и другие размеры).

row_size = int(input('Введите ширину ворот: '))
col_size = int(input('Введите высоту ворот: '))

for row in range(row_size):
    for col in range(col_size):
        if row == 0:
            print('-', end='')
        elif col == 0:
            print('|', end='')
        elif col == col_size - 1:
            print('|', end='') 
        else:
            print(' ', end='')
    print()
