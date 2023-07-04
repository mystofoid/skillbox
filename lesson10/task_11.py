# Задача 2. Цифры больше пяти
# Пользователь вводит последовательность из N чисел. Напишите программу, которая подсчитывает общее количество цифр больше пяти во всей последовательности.

numSeq = int(input('Введите последовательность чисел: '))
numeral = 5
while numeral < 0 or numeral > 9:
    numeral = int(input('Цифра должна быть от 0 до 9, повторите ввод: '))
numeralCount = 0
for num in range(numSeq):
    print('Введите', num, 'число: ', end='')
    number = int(input())
    while number > 0:
        if number % 10 > numeral:
            numeralCount += 1
        number //= 10
print('Цифр больше', numeral, 'в последовательности', numeralCount)