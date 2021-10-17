print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.

mid = 0
good = 0
overachiever = 0
pupils = int(input('Сколько учеников сегодня получили оценки 3, 4 или 5: '))
for i in range(1, pupils + 1):
    grade = int(input('Оценка для ' + str(i) + ' - го ученика: '))
    if grade == 3:
        mid += 1
    elif grade == 4:
        good += 1
    else:
        overachiever += 1
print('Троечники', mid, 'Хорошисты', good, 'Отличники', overachiever)
if mid > good and mid > overachiever or good == overachiever and mid > overachiever:
    print('Сегодня троечников больше всех')
elif good > mid and good > overachiever or mid == overachiever and good > overachiever:
    print('Сегодня хорошистов больше всех')
elif overachiever > mid and overachiever > good or mid == good and overachiever > good:
    print('Сегодня отличников больше всех')
elif mid == good and mid == overachiever:
    print('Сегодня всех оценок поровну')
elif mid == good and mid > overachiever:
    print('Сегодня кол-во хорошистов равно троечникам, а отличников меньше всего')
elif mid == overachiever and good > overachiever:
    print('Сегодня троечники и отличники равны по кол-ву, а больше всего хорошистов')
elif mid == overachiever and good < overachiever:
    print('Сегодня троечники и отличники равны по кол-ву, а меньше всего хорошистов')
elif good == overachiever and mid > overachiever:
    print('Сегодня хорошисты сравнялись с отличниками, а троечников больше всего')
elif good == overachiever and mid < overachiever:
    print('Сегодня хорошисты сравнялись с отличниками, а троечников меньше всего')
else:
    print('Нет такого условия')
    
"""
if num_1 == num_2 and num_1 == num_3:
  print('3 числа равны')
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
  print('2 числа равны')
else:
  print('0 чисел равны')
"""



