# Задача 2. Скидки!

# Напишите программу для примера, разобранного в уроке. Пользователь покупает курс стоимостью 75 000 рублей. Если денег на счету достаточно, то нужно:

# Списать со счёта деньги.
# Проверить баланс счёта. Если там меньше 5000 рублей, то зачислить на счёт 1000 рублей и вывести сообщение: «Сделана скидка».
# Вывести сообщение: «Курс успешно приобретён».
# А иначе вывести: «Не хватает денег на счету». Также в конце вывести остаток счёта и сообщение: «Хорошего дня!»

# Пример:
# Сколько денег на счету? 78500
# Курс успешно приобретён
# Сделана скидка
# Остаток на счету: 4500
# Хорошего дня!

bank = int(input('Сколько денег на счету? '))
course = 75000
discount = 1000
if bank >= 75000:
  bank -= course
  print('Курс успешно приобретен!')
  if bank < 5000:
    bank += discount
    print('Остаток на счету: ', bank)
else:
  print('На счету не достаточно денег!')
print('Хорошего дня!')
