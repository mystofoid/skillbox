# Задача 6. Стипендия
# Что нужно сделать
# Ежемесячная стипендия студента составляет educational_grant рублей, а расходы на проживание
# превышают стипендию и составляют expenses рублей в месяц.
#
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца. Обратите внимание, что
# каждый месяц цены увеличиваются на 3% относительного прошлого месяца.
#
# Составьте программу расчёта суммы денег, которую необходимо получить у родителей один раз в
# начале обучения, чтобы можно было прожить учебный год (десять месяцев), используя только эти
# деньги и стипендию.
#
# Пример
#
# Введите стипендию: 10000
#
# Введите расходы на проживание: 12000
#
# месяц траты 12000 не хватает 2000
# месяц траты 12360.0 не хватает 4360.0
# месяц траты 12730.8 не хватает 7090.8
# месяц траты 13112.7 не хватает 10203.52
# месяц траты 13506.1 не хватает 13709.63
# месяц траты 13911.2 не хватает 17620.92
# месяц траты 14328.6 не хватает 21949.55
# месяц траты 14758.4 не хватает 26708.03
# месяц траты 15201.2 не хватает 31909.27
# месяц траты 15657.2 не хватает 37566.55
# Нужно попросить у родителей 37566.55 рублей

educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))
price_growth = 0
sum_expenses = 0
sum_parents = 0
for month in range(1, 11):
    if month == 1:
        sum_expenses = expenses
        sum_parents = sum_expenses - educational_grant
        print(month, 'месяц траты', round(sum_expenses, 1), 'не хватает', round(sum_parents, 2))
    else:
        price_growth = sum_expenses * 3 / 100
        sum_expenses += price_growth
        sum_parents += sum_expenses - educational_grant
        print(month, 'месяц траты', round(sum_expenses, 1), 'не хватает', round(sum_parents, 2))
print('Нужно попросить у родителей', round(sum_parents, 2), 'рублей')