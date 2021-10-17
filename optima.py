n = int(input('Введите число: '))
for number in range(1, n // 2 + 1):
	number *= 2 #проверка на четное число вместо if
	print(number, '** 3 =', number ** 3)
