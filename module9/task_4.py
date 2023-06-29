# Задание 4. Марсоход-2
# К роботу Валли отправили «коллегу» Билли. Это его первая высадка на Марс, поэтому его тестируют в прямоугольном помещении размером 15 × 20 м. Марсоход высаживается в центре комнаты (в точке 8, 10), затем управление им передаётся оператору, то есть пользователю вашей программы. 

# Программа спрашивает, в какую сторону оператор хочет направить робота: север (клавиша W), юг (клавиша S), запад (клавиша A) или восток (клавиша D). Оператор делает выбор, марсоход перемещается в эту сторону на один метр, а программа сообщает новую позицию робота. Если марсоход упёрся в стену, он не должен пытаться переместиться в сторону стены — в этом случае его позиция не меняется. 

# Что нужно сделать
# Создайте программу для управления роботом Билли.

# Пример:

# [Программа]: Марсоход находится на позиции 6, 19, введите команду:

# [Оператор]: A

# [Программа]: Марсоход находится на позиции 5, 19, введите команду:

# [Оператор]: W

# [Программа]: Марсоход находится на позиции 5, 20, введите команду:

# [Оператор]: W

# [Программа]: Марсоход находится на позиции 5, 20, введите команду:

nord = "w"
south = "s"
west = "a"
east = "d"
latitude = 8
longitude = 10
latitudeStep = 1
longitudeStep = 1

while True:
    print(f'Марсоход находится на позиции {longitude}, {latitude}, введите команду: ')
    motion = input('Введите направление движения: ')

    if motion == nord and latitude != 15:
        latitude += latitudeStep
    elif motion == south and latitude != 0:
        latitude -= latitudeStep
    elif motion == west and longitude != 0:
        longitude -= longitudeStep
    elif motion == east and longitude != 20:
        longitude += longitudeStep