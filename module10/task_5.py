print('Задача 5. Простые числа')

#Напишите программу,
#которая считает количество простых чисел в заданной последовательности
#и выводит ответ на экран.

span = int(input("Введите размер диапазона: "))
cycle = 0
primeNumbers = []

for i in range(2, span + 1):
  for j in range(2, i):
    if i % j == 0:
      break
  else:
    primeNumbers.append(i)
    cycle += 1
print(f'Простых чисел найдено: {cycle} \nСписок простых чисел из заданного диапазона:', primeNumbers)
