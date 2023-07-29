# Задача 2. Почта 2
# На почте немного поменялись правила: теперь в почтовом извещении нужно указывать фамилию, имя, страну проживания, город, улицу, номер дома и номер квартиры.

# Реализуйте функцию, которая получает все эти данные и выводит на экран. В программе вызовите функцию три раза с разными значениями аргументов.


# Подсказка: семь аргументов.

def print_all_info(surname, name, country, town, street, house, apartment):
    print(f"\nФамилия: {surname}\n"
          f"Имя: {name}\n"
          f"Страна: {country}\n"
          f"Город: {town}\n"
          f"Улица: {street}\n"
          f"Дом: {house}\n"
          f"Квартира: {apartment}\n")



# user_surname = input("Введите фамилию: ")
# user_name = input("Введите имя: ")
# user_street = input("Введите улицу: ")
# user_house = input("Введите номер дома: ")

for _ in range(3):
    user_surname = input("Введите фамилию: ")
    user_name = input("Введите имя: ")
    user_country = input('Введите страну проживания: ')
    user_town = input('Введите город проживания: ')
    user_street = input("Введите улицу: ")
    user_house = input("Введите номер дома: ")
    user_apartment = input('Введите номер квартиры: ')
    print_all_info(user_surname, user_name, user_country, user_town, user_street, user_house, user_apartment)
