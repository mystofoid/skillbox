print('Задача 2. Я стал новым пиратом!')

#Старому капитану необходимо пополнить команду.
# Но попадут на его корабль только достойные!
# Он отобрал 10 человек и те, кто из них крикнет слово “Карамба”, попадут на борт.
#
# Пользователь вводит 10 слов.
#
# Напишите программу,
# которая определяет, сколько из них совпадают со словом “Карамба”.

phrase = 'Карамба'
cycle = 0
for i in range(10):
  text = input('Крикните как пират!: ')
  if text == phrase:
    cycle += 1
print(f'На корабль попадут только {cycle} пират(а)')


