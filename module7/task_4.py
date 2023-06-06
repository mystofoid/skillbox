# Задача 4. Успеваемость в классе
# Что нужно сделать
# В классе N человек. Каждый из них получил за урок по информатике оценку: 3, 4 или 5,
# двоек  сегодня не было.
# Напишите программу, которая получает список оценок — N чисел — и выводит на экран сообщение о
# том, кого
# сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

pupil = int(input('Сколько учеников сегодня в классе? '))
tree = 0
four = 0
five = 0
for num in range(pupil):
    value = int(input('Какую оценку поставить?: '))
    if value == 3:
        tree += 1
    elif value == 4:
        four += 1
    elif value == 5:
        five += 1
    else:
        print('Сегодня двойки и колы ставить нельзя')
if tree < four and four > five:
    print('Хорошистов сегодня больше', four)
elif five < tree and tree > four:
    print('Троечников сегодня больше', tree)
elif four < five and five > tree:
    print('Отличников сегодня больше', five)
elif tree == four and tree != five:
    print('Троечников и хорошистов поровну, по', tree, four)
elif tree == five and tree != four:
    print('Троечников и отличников поровну, по', tree, five)
elif four == five and four != tree:
    print('Хорошистов и отличников поровну, по', four, five)
else:
    print('Всех поровну')

print('Троек:', tree)
print('Четверок', four)
print('Пятерок', five)