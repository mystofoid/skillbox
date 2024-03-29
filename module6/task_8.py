# Задача 8. Игра «Компьютер угадывает число»
# Что нужно сделать
# Поменяйте мальчика и компьютер из прошлой задачи местами. Теперь мальчик загадывает число
# между 1  и 100 (включительно). Компьютер может спросить у мальчика: «Твоё число равно,
# меньше  или больше, чем число N?», где N — число, которое хочет проверить компьютер. Мальчик
# отвечает одним из трёх чисел: 1 — равно, 2 — больше, 3 — меньше.

# Напишите программу, которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.
# Подсказка
# Используйте бинарный поиск, а не конкатенацию.

# human_number = int(input('Введите ваше число(от 1 до 100 вкл.): '))
# count = 0
# num = 0
# while num != human_number:
#     num = int(input('Введите число: '))
#     if num < human_number:
#         count += 1
#         print('Искомое число больше: ')
#     elif num > human_number:
#         count += 1
#         print('Искомое число меньше: ')
#     else:
#         count += 1
#         print('Вы угадали число')
#         print(count)
left = 0
right = 101
count = 0
while True:
    num = (left + right) // 2
    print('Твое число равно, меньше или больше, чем число', num, '?')
    answer = int(input('1 - равно; 2 - меньше; 3 - больше '))
    count += 1
    if answer == 1:
        print('Угадал с ', count, 'раза!')
        break
    elif answer == 2:
        right = num
        print(num, '2')
    elif answer == 3:
        left = num
        print(num, '3')