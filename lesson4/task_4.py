# Задача 1. Курс от Skillbox-2

# Напишите программу для примера, разобранного в уроке.

# Пользователь покупает курс стоимостью 75 000 рублей.
# Если денег на счету достаточно, нужно списать деньги и вывести сообщение: «Курс успешно приобретён», — а иначе вывести: «Не хватает денег на счёте».
# Не забудьте пожелать «Хорошего дня!» в любом случае. Мы же вежливые продавцы.


# Пример:

# Сколько денег на счету? 5000

# Не хватает денег на счету.

# Хорошего дня!
bank = int(input('Сколько денег на счету?: '))
course = 75000
if bank >= course:
  bank -= course
  print('Курс успешно приобретен!')
else:
  print('Не хватает денег на счёте')
print('Хорошего дня!')
