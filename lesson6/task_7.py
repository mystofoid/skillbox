# Задача 1. Неправильный таймер
#
# Петя писал таймер для телефона, но у него что-то пошло не так.
#
# count = 0
# While count <= 10
#  if count == 0:
#    print('Время вышло!')
#  else:
#    print(count)
#    count -= 1
#
# Скопируйте программу в редактор, исправьте ошибки и убедитесь, что на экран выводятся числа с 10
# до 0 и сообщение «Время вышло!».

#  ver 1
# count = 10
# while count <= 10:
#     print(count)
#     count -= 1
#     if count == 0:
#         print(count)
#         print('Время вышло!')
#         break

# ver 2
count = 10
while count <= 10:
    if count == 0:
        print(count)
        print('Время вышло!')
        break
    else:
        print(count)
        count -= 1
