# Задача 3. Лотерея 2
# Напишите программу для немного усложнённой версии задачи про выигрышные билеты. Есть заранее
# известные номера билетов: 345, 19, 87, 1020 и 421 (можете брать свои номера, не стесняйтесь).
# Теперь, билет считается выигрышным, если номер билета - трёхзначное число и оно делится на  5.
# Выведете в консоль сообщение для каждого выигрышного билета и количество победителей.
#
winners = 0
for number in 345, 19, 87, 1020, 421, 555, 23, 675:
    if number % 5 == 0 and number % 1000 == number:
        print('Счастливый билет', number)
        winners += 1
print('Колличество счастливых билетов:', winners)
