# Задача 3. Лестница чисел
# Пользователь вводит число N. Напишите программу, которая по этому числу выводит вот такую лестницу из чисел:
# Введите размер матрицы: 5
# 0 1 2 3 4 5
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5
size = int(input('Введите размер матрицы: '))

for row in range(size + 1):
  for col in range(row, size + 1):
    print(col, end= ' ')
  print()
