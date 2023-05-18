# Задача 1. Яблоки

# Транспортная компания ООО «ФруктыТрансСервис» занимается логистикой и грузоперевозками фруктов. Программисту Владимиру дали задачу написать программное обеспечение, которое позволит понять, сколько фруктов можно загрузить и сколько останется на складе.

# Напишите программу, которая решает задачу из урока: у транспортной компании есть 41 тонна яблок, которые нужно разместить по ящикам. Каждый ящик вмещает в себя три тонны. Необходимо выяснить, сколько ящиков мы сможем заполнить и сколько яблок останется. Оба ответа нужно вывести на экран.

apples = 41 # 41 тонна яблок
boxes = 3 # 3 тонны яблок вмещается в 1 ящик
full_boxes = apples // boxes
rest_apples = apples % boxes
print('Полных ящиков: ', full_boxes)
print('Остаток тонн яблок: ', rest_apples)
