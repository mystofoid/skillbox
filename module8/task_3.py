print('Задача 3. Это будет бомба')

# Мы разрабатываем пошаговую игру по мотивам боевика.
# Игрок - главный герой и должен обезвредить бомбу, которая взорвётся через N секунд.
# Программа спрашивает пользователя хочет ли он обезвредить бомбу сейчас.
#
# Если ответ “0” (то есть “нет”), то счетчик бомбы уменьшается.
# Если он достиг нуля, то программа выдаёт сообщение “Бомба взорвалась”,
# а если не достиг, то программа вновь переспрашивает,
# не хочет ли игрок обезвредить бомбу, и сообщает, сколько времени осталось до взрыва..
#
# Если ответ “да”, то программа выводит на экран сообщение о том,
# что бомба обезврежена и сколько секунд оставалось до взрыва.
# Используйте цикл for.

time = int(input('Сколько секунд установить на таймер? '))
defuse = int(input('Хотите ли вы обезвредить бомбу сейчас?(Да - 1; Нет - 0) '))
if defuse == 0:
  for i in range(time, 0, -1):
    print('До взрыва осталось', i, 'секунд')
    if i != 0:
      defuse = int(input('Не хотите ли вы опять обезвредить бомбу?(Да - 1; Нет - 0) '))
      if defuse == 1:
          print('Бомба обезврежена', i, 'секунде')
          break
      elif i == 1:
        print('Бомба взорвалась')
else:
  print('Бомба обезврежена')
