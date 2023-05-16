# Задача 7. Хватит ли зарплаты
# Что нужно сделать

# Вася набрался опыта и решил поискать вакансию с большей зарплатой. Его привлекла вакансия со странной формулой для расчёта заработной платы:

# Он хочет понять, сколько часов нужно отработать, чтобы хватило на погашение кредита и еду.

# Напишите программу, которая запрашивает у пользователя три числа: количество отработанных часов, остаток по кредиту и количество денег на еду. После этого рассчитывается зарплата по формуле. Если зарплата больше или равна сумме, которая требуется на кредит и еду, то выводится сообщение: «Часов хватает. Можно отдохнуть». В противном случае: «Часов не хватает. Придётся работать больше!»



# Пример:
# Введите отработанные часы: 80
# Введите остаток по кредиту: 1000
# Введите траты на еду: 5000
# Часов не хватает. Придётся работать больше!

hours = int(input('Количество отработанных часов: '))
balance = int(input('Остаток по кредиту: '))
food = int(input('Количество денег на еду: '))
salary = (200 * hours) / (2 ** 3) + hours
if salary >= balance + food:
    print('Часов хватает. Можно отдохнуть.')
else:
    print('Часов не хватает. Придется поработать больше!')