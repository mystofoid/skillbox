print('Задача 4. Первая цифра')

# Дано положительное действительное число(вещественное число) X.
# Выведите его первую цифру после десятичной точки.
# При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками

number = float(input("Введите вещественное число: "))
temp = number
digit = 0
number = round(number, 2) * 10
digit = int(number % 10)
print(f"Первая цифра после десятичной точки числа {temp} равна {digit}")
