print('Задача 1. Календарь')

# Мы продолжаем разрабатывать удобный календарь для смартфона.
# Функцию определения високосного года мы добавили,
# но забыли ещё много разных очевидных вещей.
#
# Напишите программу,
# которая принимает от пользователя день недели в виде строки и выводит его номер на экран.
#
# Пример:
# Введите день недели: вторник
# Номер дня недели: 2

# !!!Через список горазда проще, но сделал и через условные операторы, т.к. списки еще не проходили.!!!
# weekDay = input('Введите день недели: ')
# week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# cycle = 0
# for day in week:
#   cycle += 1
#   if day == weekDay:
#     print('Номер недели:', cycle)
#     break

day_1 = 'Понедельник'
day_2 = 'Вторник'
day_3 = 'Среда'
day_4 = 'Четверг'
day_5 = 'Пятница'
day_6 = 'Суббота'
day_7 = 'Воскресенье'
weekDay = input('Введите день недели: ')
if weekDay == day_1:
  print('Номер дня недели:', 1)
elif weekDay == day_2:
  print('Номер дня недели:', 2)
elif weekDay == day_3:
  print('Номер дня недели:', 3)
elif weekDay == day_4:
  print('Номер дня недели:', 4)
elif weekDay == day_5:
  print('Номер дня недели:', 5)
elif weekDay == day_6:
  print('Номер дня недели:', 6)
elif weekDay == day_7:
  print('Номер дня недели:', 7)
else:
  print('Вы ввели не день недели!')
