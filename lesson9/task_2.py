# Задача 2. Начальник
# Напишите программу для робота-начальника. Он спрашивает у пользователя, выполнил ли он задание, которое выдавал вчера, и 
# продолжает это делать до тех пор, пока тот не ответит ему “Да, конечно, сделал”.

answer = 'Да, конечно, сделал'
answer_human = ''
while answer != answer_human:
    answer_human = input('Вы выполнили задание? ')