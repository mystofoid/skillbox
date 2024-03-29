# Задача 3. Поел — можно и поспать, поспал — можно и поесть
# Напишите программу, разобранную в уроке.
#
# У Саши интересный режим сна: он может проснуться когда угодно, хоть ночью, но засыпает всегда до
# того, как наступит полночь, обычно в 23 часа. А ещё он очень любит поесть. Он ест каждый час и
# если съедает больше 2000 калорий, то он просто падает спать. Напишите программу, которая поможет
# Саше понять, всё ли с ним хорошо. Для этого нужно посчитать, сколько он всего съест калорий и
# сколько часов будет бодрым.
#
awake_time = int(input('Во сколько проснулся? '))
hoursVivacity = 0
calories = 0
totalCalories = 0
for num in range(awake_time, 23):
    print('Сейчас', num, 'час(ов).')
    calories = int(input('Сколько съел калорий? '))
    totalCalories += calories
    if totalCalories > 2000:
        print('Саша заснул.')
        break
    hoursVivacity += 1
print('Саша бодрствовал', hoursVivacity, 'и съел', totalCalories, 'калорий')
