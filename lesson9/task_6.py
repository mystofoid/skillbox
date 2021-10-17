# Задача 3.

# Мы входим в команду разработки нового текстового редактора и нам поручили разработать для него подсчёт нужного символа в тексте, а именно - буквы Ы. Причём отдельно с верхним регистром и отдельно с нижним.
# Напишите программу, которая считает количество больших и количество маленьких букв Ы в тексте и выводит ответ на экран.
# Пример:
# Введите текст: Прыг скок
# Больших букв Ы: 0
# Маленьких букв Ы: 1

text = input('Введите текст ')
firstSimbol = input('Введите символ который нужно посчитать ')
secondSimbol = input('Введите символ который нужно посчитать ')
countFirstSimbol = 0
countSecondSimbol = 0

for symbol in text:
  if symbol == firstSimbol:
    countFirstSimbol += 1
  if symbol == secondSimbol:
    countSecondSimbol += 1

print('Больших букв', firstSimbol, 'равно', countFirstSimbol)
print('Маленьких букв', secondSimbol, 'равно', countSecondSimbol)
