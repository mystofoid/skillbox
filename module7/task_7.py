# Задача 7. Пропавшая карточка
# Что нужно сделать
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась.
# Напишите программу, которая поможет найти потерянную карточку, если номера оставшихся известны.
# Найдите её, зная номера оставшихся карточек.
#
# Введите число карточек — N.
#
# Затем введите N − 1 номера оставшихся карточек. Они могут быть введены в любом порядке.
#
# Пример:
#
# Введите количество карточек: 5
# Введите номер оставшейся карточки: 1
# Введите номер оставшейся карточки: 4
# Введите номер оставшейся карточки: 5
# Введите номер оставшейся карточки: 3
# Номер пропавшей карточки: 2
carts = int(input('Введите кол-во карточек: '))
summ = 0
summ_2 = 0
# for i in range(1, carts + 1):
#     summ += i
summ = (1 + carts) / 2 * carts # арифметическая прогрессия
print(summ)
for i in range(1, carts):
    cart = int(input('Введите номер оставшейся карточки: '))
    summ -= cart # избавились от лишней переменной findCard
# findCard = summ - summ_2
print('Номер пропавшей карточки:', summ)