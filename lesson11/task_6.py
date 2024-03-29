# Задача 3. Точность и аккуратность
# Робот из задачи “Компьютерное зрение” правильно определяет на какой клетке стоят фигуры. Но вот беда, часто по вине соперника-человека фигуры стоят на доске не ровно по центру клетки, а со смещением. Если во время игры такое смещение станет слишком велико, то станет непонятно в какой клетке стояла фигура. Чтобы избежать этой ситуации нужно чтобы робот поправлял фигуры на доске, выставляя их по центру клетки. Модифицируйте программу “Компьютерное зрение” так, чтобы она выдавала не только номера клетки, в которой находится фигура но и две вещественных поправки: на сколько нужно подвинуть фигуру по горизонтали и вертикали для того чтобы она оказалась по центру своей клетки.

# Пример:

# Введите местоположение фигуры
# По горизонтали: 0.731
# По вертикали: 0.167
# Фигура находится в клетке (7, 1)
# Поправьте положение фигуры на (0.019, -0.017)

print('Введите местоположение фигуры')
coordinate_x = float(input('По горизонтали: '))
coordinate_y = float(input('По вертикали: '))

while 0.8 < coordinate_x and coordinate_y < 0:
    print('Клетки с такой координатой не существует', '\nПовторите ввод: ')
    coordinate_x = float(input('По горизонтали: '))
    coordinate_y = float(input('По вертикали: '))

x = int(coordinate_x * 10)
y = int(coordinate_y * 10)
print(f'Фигура находится в клетке ({x}, {y})')

x_center = x * 0.1 + 0.05
y_center = y * 0.1 + 0.05
x_drift = round(x_center - coordinate_x, 3)
y_drift = round(y_center - coordinate_y, 3)
print(f"Поправьте положение фигуры на ({x_drift}, {y_drift})")