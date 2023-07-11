# Задание 4. Простые числа
# Что нужно сделать

# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.

# Простое число делится только на себя и на единицу. Последовательность задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна итерация — одно число.

# Пример:

# Введите количество чисел: 6.
# Введите число: 4.
# Введите число: 7.
# Введите число: 20.
# Введите число: 3.
# Введите число: 11.
# Введите число: 37.

# Количество простых чисел в последовательности: 4.

# queue = int(input('Введите количество чисел: '))
# count = 0
# for num in range(queue):
#     number = int(input('Введите число: ')) #27644437 простое число
#     isPrime = True
#     for divider in range(2, number):
#         if number % divider == 0:
#             print('Делится на', divider)
#             isPrime = False
#             break
#     if isPrime:
#         count += 1
#         print(number, '- простое число')
#     else:
#         print(number, '- составное число')
# print('Простых чисел в последовательности ввода:', count)

span = int(input("Введите размер диапазона чисел: "))
cycle = 0
primeNumbers = []

for i in range(2, span + 1):
  for j in range(2, i):
    if i % j == 0:
      break
  else:
    primeNumbers.append(i)
    cycle += 1
print(f'Простых чисел найдено: {cycle} \n Список простых чисел из заданного диапазона:', primeNumbers)
































































 











































