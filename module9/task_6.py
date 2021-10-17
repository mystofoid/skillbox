print('Задача 6. Спецшифр')

# Два сотрудника спецслужб переписываются необычным шифром.
# Каждую букву они шифруют в виде строки,
# внутри которой есть длинная последовательность букв “s”,
# а длина самой длинной - это и есть номер буквы алфавита, которую хотят отправить.
#
# Напишите программу,
# которая получает на вход строку,
# подсчитывает в ней самую длинную последовательность подряд идущих букв “s” и выводит ответ на экран.
#
# Пример:
# Введите строку: ssbbbsssbc
# Самая длинная последовательность: 3

# идём циклом по строке
# if символ == s:
#    нынешняя_посл += 1
# elif нынешняя_посл > максимальной_посл:
#		максимальная_посл = нынешняя_посл
#		нынешняя_посл = 0
# Задача 6: сейчас при завершении строки на самой длинной последовательности из s она не заcчитается - обновлять значение самой длинной последовательности надо в другом месте.

text = input('Введите строку: ')
sequence = 0
sequenceMax = 0

for i in text:
  if i == 's':
    sequence += 1
    if sequence > sequenceMax:
      sequenceMax = sequence
  else:
    sequence = 0
print('Самая длинная последовательность:', sequenceMax)
