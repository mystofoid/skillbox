# Задача 2. Функция
# Что нужно сделать
# Учитель математики придумывает каждому ученику отдельные функции, которые нужно отобразить на графике и посчитать. Ещё учитель разбирается в программировании, и чтобы не считать вручную эти функции, он написал программу, которая делает работу за него.

# Напишите программу, которая получает от пользователя число X и вычисляет значение функции Y по следующей схеме:

# y = {(x − 12, x > 0), (5,  x = 0), (x ** 2,  x < 0)

# Напомним, как это работает: 

# для X > 0, Y = X − 12
# для X = 0,  Y = 5
# для X < 0, Y = X ** 2

# Пример:
# Введите икс: 0
# Игрек равен 5

# Пример 2:
# Введите икс: −6
# Игрек равен 36

x = int(input('Введите значение икс: '))
y = 0
if x > 0:
    y = x - 12
    print('Игрек равен ', y)
elif x == 0:
    y = 5
    print('Игрек равен ', y)
else:
    y = x ** 2
    print('Игрек равен ', y)