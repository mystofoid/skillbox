print('Задача 7. Стипендия')

# Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
#
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.

educational_grant = int(input('Введите сумму стипендии: '))
expenses = int(input('Введите сумму расходов: '))
totalExpenses = 0
totalEdu_grand = 0
parentsMoney = 0
for month in range(1, 11):
    totalEdu_grand += educational_grant
    if month == 1:
        expenses_1 = expenses
        print(month, '- й месяц: затраты', expenses)
        continue
    totalExpenses += int(expenses)
    expenses += expenses * 3 / 100
    print(month, '- й месяц: затраты', int(expenses))
totalExpenses += expenses_1
print('Всего затрат', totalExpenses, 'рублей')
print('Всего получишь степендии', totalEdu_grand, 'рублей')
parentsMoney = totalExpenses - totalEdu_grand
print('Нужно поросить у родителей сумму', parentsMoney, 'рублей')
