# Задача 3. Фальшивомонетчики

# Пете дали три монетки и сказали, что если он сможет на весах без гирь определить, какая из них фальшивая (более лёгкая), то сможет забрать их все. А Петя в одной из книжек прочитал, что для этого достаточно одного взвешивания: если две монеты весят одинаково, то фальшивая третья, а иначе фальшивая та, которая легче на весах. Напишите программу, которая принимает на вход вес трёх монет (две одинаковые, третья меньше) и определяет, какая из них легче.

coin_1 = int(input('Вес первой монеты: '))
coin_2 = int(input('Вес второй монеты: '))
coin_3 = int(input('Вес третьей монеты: '))
if coin_1 == coin_2:
    print('Вес 1 и 2 монеты совпал')
    print('Третья монета фальшивая и весит ', coin_3, 'грамм')
elif coin_1 == coin_3:
    print('Вес 1 и 3 монеты совпал')
    print('Вторая монета фальшивая и весит ', coin_2, 'грамм')
else:
    print('Первая монета фальшивая и весит ', coin_1, 'грамм')