
# Задание 7. Пирамидка-2
# Что нужно сделать
# Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран, заполняя нечётными числами:

#                 1
#             3       5
#         7       9      11
#     13      15      17      19
# 21      23      25      27      29

size = int(input('Введите высоту пирамиды: '))
numeral = 1

print(end='\n')

for row in range(size):
    space = size - row - 1 # отвечает за пустоты перед числами
    print('    ' * space, end= '')
    for col in range(row + 1):
        if numeral == 3 or numeral == 7:
            indent = 7 # число определено опытным путем, чтобы пирамида была симетричной
        elif numeral >= 9 and numeral < 101:
            indent = 6 # аналогично предыдущему комментарию
        else:
            indent = 5
        print(numeral, end= ' ' * indent)
        numeral += 2
    print()




