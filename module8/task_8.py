# Задача 8. Кинотеатр
# Что нужно сделать
# X мальчиков и Y девочек пошли в кинотеатр и купили билеты на идущие подряд места в одном ряду.
# Напишите программу, которая выдаст, как нужно сесть мальчикам и девочкам, чтобы рядом с каждым
# мальчиком сидела хотя бы одна девочка, а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа: количество мальчиков X и количество девочек Y. В ответе выведите
# какую-нибудь строку, в которой будет ровно X символов B, обозначающих мальчиков, и Y символов G,
# обозначающих девочек, удовлетворяющую условию задачи. Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно, выведите строку
# «Нет решения».
#
# Пример 1
# Введите количество мальчиков: 5
# Введите количество девочек: 5
#
# Ответ: BGBGBGBGBG
#
# Пример 2
# Введите количество мальчиков: 5
# Введите количество девочек: 3
#
# Ответ: BGBGBBGB
#
# Пример 3
# Введите количество мальчиков: 100
# Введите количество девочек: 1
#
# Ответ: Нет решения
'''
boy = int(input("Введите количество мальчиков: "))
girl = int(input("Введите количество девочек: "))
total = boy + girl
count = count_boy = count_girl = 0
if boy == girl:
    print(" Мальчиков и девочек поровну.")
    print("BG" * boy)
elif boy * 2 < girl or girl * 2 < boy:
   print("Нет решения.")
else:
    while boy != girl:
        while boy > girl:
            count += 1
            boy -= 2
            girl -= 1
            count_boy += 1
        while girl > boy:
            count += 1
            girl -= 2
            boy -= 1
            count_girl += 1
    count = int((total - count * 3) / 2)
    print("BG" * count, "BGB" * count_boy, "GBG" * count_girl)
'''
boy = int(input("Введите количество мальчиков: "))
girl = int(input("Введите количество девочек: "))
result = ''
if boy > 2 * girl or girl > 2 * boy:
    print('Нет решения')
elif boy >= girl:
    k = boy - girl # кол-во BGB
    for bgb in range(k):
        result += 'BGB'
    for bg in range(girl - k): # (girl - k) кол-во BG
        result += 'BG'
else:
    k = girl - boy
    for gbg in range(k):
        result += 'GBG'
    for gb in range(boy - k):
        result += 'GB'
print(result)
