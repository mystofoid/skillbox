'''
Задача 3. Диета

Саша просыпается когда угодно, но в 23 часа уже точно идёт спать. Питается Саша следующим образом: каждые 3 часа он выпивает литр воды и съедает N калорий. Пить и есть он, кстати, начинает сразу как только проснётся. Напишите программу, которая считает сколько он выпьет литров воды и сколько калорий он съест перед тем как пойдёт спать.
'''
wake_up = int(input('Во сколько Саша проснулся? '))
water = 0
calories_sum = 0
for hour in range(wake_up, 23, 3):
  water += 1
  print('Сейчас', hour, 'часа(ов)')
  calories = int(input('Сколько калорий Саша съел? '))
  print('Выпил', water, 'литр(а,ов) воды')
  calories_sum += calories
print('Выпито воды', water)
print('Съедено калорий', calories_sum)
