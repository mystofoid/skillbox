print('Задача 8. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.


year = 0
y = 100000
p = 50 / 100 # процент годовых
x = int(input('Сколько вы планируете внести на счет? '))
while x < y:
	year += 1
	x = x + x * p
	print(x)
print('Прошло', year, 'года(лет) и счет стал равен ', int(x))

