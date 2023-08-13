# Задача 7. Недоделка
# Что нужно сделать
# Вы пришли на работу в компанию по разработке игр, целевая аудитория — дети и их родители. У предыдущего программиста было задание сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них. Однако программист, на место которого вы пришли, перед увольнением не успел выполнить эту задачу и оставил только небольшой шаблон проекта. Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».

# Правила игры «Камень, ножницы, бумага»: программа запрашивает у пользователя строку и выводит, победил он или проиграл. Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.

# Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор, пока он не отгадает загаданное.

from random import randint
from random import choice

def rock_paper_scissors():
  while True:
    user_action = input('\nСделайте выбор - камень, ножницы или бумага: ')
    possible_actions = ["камень", "бумага", "ножницы"]
    computer_action = choice(possible_actions)
    print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.\n")
    if user_action == computer_action:
        print(f'Оба юзера выбрали {user_action}. Ничья!')
    elif user_action == 'камень':
        if computer_action == 'ножницы':
            print('Камень бьет ножницы! Вы победили!')
        else:
            print('Бумага оборачивает камень! Вы проиграли.')
    elif user_action == 'бумага':
        if computer_action == 'камень':
            print('Бумага оборачивает камень! Вы победили!')
        else:
            print('Ножницы режут бумагу! Вы проиграли.')
    elif user_action == 'ножницы':
        if computer_action == 'бумага':
            print('Ножницы режут бумагу! Вы победили!')
        else:
            print('Камень бьет ножницы! Вы проиграли.')

    play_again = '' 
    play_again = input('\nСыграем еще? (д/н): ') 
    if play_again.lower != 'д': 
        break 

def guess_the_number():
    count = 0
    begin = 1
    end = 100
    random_integer = randint(begin, end)
    your_integer = int(input('Угадайте число от 1 до 100: '))
    while random_integer != your_integer:
        count += 1
        your_integer = int(input('Повторите попытку: '))
        if random_integer > your_integer:
            begin = your_integer
            print('Ваше число меньше чем задумал компьютер')
            print(f'Алгоритм бинарного поиска рекомендует вам число: {round((end + begin) / 2)}')
        elif random_integer < your_integer:
            end = your_integer
            print('Ваше число больше чем задумал компьютер')
            print(f'Алгоритм бинарного поиска рекомендует вам число: {round((end + begin) / 2)}')
        else:
            print('Вы угадали!')
            print(f'Число которое задумал компьютер {random_integer}, число которое вы угадали {your_integer} с попытки {count}')

def mainMenu():
    while True:
        try:
            choice = int(input('"Введите цифру 1 - если хотите игру «Камень, ножницы, бумага»\nВведите цифру 2 - если хотите игру «Угадай число»\n: '))
            if choice == 1:
                rock_paper_scissors()
            elif choice == 2:
                guess_the_number()
            else:
                print('Ошибка ввода.')
            break
        except ValueError:
            print('Вы ввели не целое число или не число. Повторите ввод.')
            mainMenu()

mainMenu()