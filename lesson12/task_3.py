'''
Задача 3. Почта

Василий пришёл получать посылку на почту. Разумеется, в почтовом извещении ему нужно было написать свои фамилию, имя и адрес проживания, чтобы кто-нибудь не получил посылку за него, например члены его семьи (а им бы хотелось!).

Напишите функцию для вывода фамилии, имени и адреса для конкретного члена семьи. Выведите информацию о нём три раза (без цикла).

Пример результата:

Фамилия: Иванов
Имя: Василий
Улица: Пушкина
Дом: 32


Фамилия: Иванов
Имя: Василий
Улица: Пушкина
Дом: 32


Фамилия: Иванов
Имя: Василий
Улица: Пушкина
Дом: 32
'''

def date_person():
	print("\n Фамилия:", surname, "\n Имя:", name, "\n Улица:", street, "\n Дом:", house)
	print("\n Фамилия:", surname, "\n Имя:", name, "\n Улица:", street, "\n Дом:", house)
	print("\n Фамилия:", surname, "\n Имя:", name, "\n Улица:", street, "\n Дом:", house)

surname = input("Введите вашу фамилию: ")
name = input("Введите ваше имя: ")
street = input("Введите вашу улицу: ")
house = int(input("Введите номер вашего дома: "))

date_person()


