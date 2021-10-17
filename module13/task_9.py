print('Задача 9. Аннуитетный платёж')


# Кредит в сумме S млн руб.,
# выданный на n лет под i% годовых,
# подлежит погашению равными ежегодными выплатами в конце каждого года,
# включающими процентные платежи и сумму в погашение основного долга.
#
# Проценты начисляются в один раз в год.
# После выплаты третьего платежа
# достигнута договорённость между кредитором и заёмщиком
# о продлении срока погашения займа на n_2 лет
# и увеличении процентной ставки с момента конверсии до i_2%.
#
# Напишите программу,
# которая выводит план погашения оставшейся части долга.
#
# A = KS
#
# K = i(1 + i) ** n / (1 + i) ** n - 1
#
# Пример:
#
# Введите сумму кредита: 40e6
# На сколько лет выдан? 5
# Сколько процентов годовых? 6
#
# Период: 1
#
# Остаток долга на начало периода: 40000000.0
# Выплачено процентов: 2400000.0
# Выплачено тела кредита: 7095856.02
#
#
# Период: 2
#
# Остаток долга на начало периода: 32904143.98
# Выплачено процентов: 1974248.6387999998
# Выплачено тела кредита: 7521607.3812
#
# Период: 3
#
# Остаток долга на начало периода: 25382536.5988
# Выплачено процентов: 1522952.195928
# Выплачено тела кредита: 7972903.824072
#
# Остаток долга: 17409632.774728
#
# =================================================
#
# На сколько лет продляется договор? 2
# Увеличение ставки до: 10
#
# Период: 1
#
# Остаток долга на начало периода: 17409632.774728
# Выплачено процентов: 1740963.2774728
# Выплачено тела кредита: 3751267.5625271997
#
# Период: 2
#
# Остаток долга на начало периода: 13658365.2122008
# Выплачено процентов: 1365836.52122008
# Выплачено тела кредита: 4126394.3187799198
#
# Период: 3
#
# Остаток долга на начало периода: 9531970.89342088
# Выплачено процентов: 953197.0893420881
# Выплачено тела кредита: 4539033.750657911
#
# Период: 4
#
# Остаток долга на начало периода: 4992937.142762969
# Выплачено процентов: 499293.71427629696
# Выплачено тела кредита: 4992937.125723703
#
# Остаток долга: 0.017039266414940357
'''
def conversion():
  summ_credit = float(input('Введите сумму кредита: '))
  years = int(input('На сколько лет выдан: '))
  procent = float(input('Сколько процентов годовых? '))
  procent /= 100
  year_procent = procent
  body_credit = 0
  years_rest = years
  for data in range(1, years + 1):
    if data < 4:
      k = procent * (1 + procent) ** years_rest / ((1 + procent) ** years_rest - 1)
      years_rest -= 1
      a = summ_credit * k
      round(a, 2)
      year_procent *= summ_credit
      body_credit = a - year_procent
      print(f'\nПериод: {data}')
      print(f'Остаток долга на начало периода: {summ_credit}')
      summ_credit += year_procent - a
      print(f'Выплачено процентов: {year_procent}')
      print(f'Выплачено тело кредита: {body_credit}\n')
    year_procent = procent
    body_credit = 0
  print(f'Остаток долга: {summ_credit}')
  print('=' * 35)
  return rest_loan(summ_credit, years)


def rest_loan(sum_credit, years):
  extension = int(input('\nНа сколько лет продляется договор? '))
  bet = int(input('Увеличение ставки до: '))
  bet /= 100
  year_procent = bet
  years = years_rest = (years - 3) + extension
  for data in range(1, years + 1):
    if data < years + 1:
      k = bet * (1 + bet) ** years_rest / ((1 + bet) ** years_rest - 1)
      years_rest -= 1
      a = sum_credit * k
      round(a, 2)
      year_procent *= sum_credit
      body_credit = a - year_procent
      print(f'\nПериод: {data}')
      print(f'\nОстаток долга на начало периода: {sum_credit}')
      sum_credit += year_procent - a
      print(f'Выплачено процентов: {year_procent}')
      print(f'Выплачено тело кредита: {body_credit}')
      year_procent = bet
      body_credit = 0
    else:
      k = bet * (1 + bet) ** years_rest / ((1 + bet) ** years_rest - 1)
      years_rest -= 1
      a = sum_credit * k
      round(a, 2)
      year_procent *= sum_credit
      body_credit = a - year_procent
      print(f'\nПериод: {data}')
      print(f'Остаток долга на начало периода: {sum_credit}')
      sum_credit -= body_credit
      print(f'Выплачено процентов: {year_procent}')
      print(f'Выплачено тело кредита: {body_credit}')
  print(f'\nОстаток долга: {sum_credit}')

conversion()
'''


def period_printout(summ, percent, a_payment, period):
  for i in range(1, period + 1):
    paid_percent = summ * percent
    paid_credit = a_payment - paid_percent
    print('\nПериод', i)
    print('\nОстаток долга на начало периода:', summ)
    print('Выплачено процентов:', paid_percent)
    print('Выплачено тела кредита:', paid_credit)
    summ -= paid_credit
  else:
    print('\nОстаток долга:', summ)

  return summ


def payment(summ, year, percent):
  k = (percent * (1 + percent) ** year) / ((1 + percent) ** year - 1)
  a_payment = round(k * summ, 2)

  return a_payment


credit = float(input('\nВведите сумму кредита: '))
years = int(input('На сколько лет выдан: '))
percent_per_year = int(input('Сколько процентов годовых: '))
percent_per_year /= 100
period = 3

A = payment(credit, years, percent_per_year)
balance = period_printout(credit, percent_per_year, A, period)
period = years - period

print('\n' + '=' * 50)
years = int(input('\nНа сколько лет продляется договор?: '))
period += years
percent_per_year = int(input('Увеличение ставки до: '))
percent_per_year /= 100

A = payment(balance, period, percent_per_year)
period_printout(balance, percent_per_year, A, period)
