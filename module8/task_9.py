print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения

# ((x-1)(x-3)(x-7)…(x-63)/ # нечетные numerator
# ((x-2)(x-4)(x-8)…(x-64)) # четные denominator
#'''
x = int(input('Введите значение X: '))
result = 1
for number in range(1, 7):
  result *= (x - (2 ** number - 1)) / (x - (2 ** number))
print(f'Результат выражения равен {result}')
'''
x = int(input('Введите значение X: '))
answer = 1
numerator = 1
denominator = 1
for number in range(1, 7):
  numerator *= (x - (2 ** number - 1))
  denominator *= (x - 2 ** number)
answer = numerator / denominator
print(f'Результат выражения равен {answer}')
'''
