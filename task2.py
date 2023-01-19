# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

from random import randint


def check_int(question=str):  # проверка на ввод числа
    data = input(question)
    while ((not data.isdigit()) or int(data) > 10 or int(data) == 0):
        data = input(f"Ошибка ввода! \n {question}")
    return int(data)


def lottery(name_1, name_2):
    lottery_num = randint(1, 2)
    if lottery_num != 1:
        name_1, name_2 = name_2, name_1
    return (name_1, name_2)


def print_pole(pole_1, pole_2, pole_3):
    print(*pole_1, sep="|")
    print(*pole_2, sep="|")
    print(*pole_3, sep="|")


def step_by_step(num, pole=list, sign=str):
    if num in pole:
        i = pole.index(num)
        pole[i] = sign
    return pole


def winner_game(pole_1, pole_2, pole_3):
    winner = False
    if pole_1[0] == pole_1[1] == pole_1[2] or \
            pole_2[0] == pole_2[1] == pole_2[2] or \
            pole_3[0] == pole_3[1] == pole_3[2] or \
            pole_1[0] == pole_2[0] == pole_3[0] or \
            pole_1[1] == pole_2[1] == pole_3[1] or \
            pole_1[2] == pole_2[2] == pole_3[2] or \
            pole_1[0] == pole_2[1] == pole_3[2] or \
            pole_1[2] == pole_2[1] == pole_3[0]:
        winner = True
    return winner


def game(name_1, name_2):
    row_1 = [x for x in range(1, 4)]
    row_2 = [x for x in range(4, 7)]
    row_3 = [x for x in range(7, 10)]
    row_all = [x for x in range(1, 10)]
    print_pole(row_1, row_2, row_3)

    turn = True
    count = 0
    while not winner_game(row_1, row_2, row_3) and len(row_all) > 0:
        if turn == True:
            name = name_1
            char = "X"
        else:
            name = name_2
            char = "0"
        if name != "бот":
            q = f"{name}, куда ставим {char}: "
            step = check_int(q)
            while not (step in row_1 or step in row_2 or step in row_3):
                print("Это поле уже занято!")
                step = check_int(q)
        else:
            # бот без интеллекта:
            i = randint(0, len(row_all) - 1)
            step = row_all[i]
            print(f'{name} выбрал поле {step}')

        row_1 = step_by_step(step, row_1, char)
        row_2 = step_by_step(step, row_2, char)
        row_3 = step_by_step(step, row_3, char)

        print_pole(row_1, row_2, row_3)
        turn = not turn
        row_all.remove(step)

    if winner_game(row_1, row_2, row_3):
        print(f"Победил {name}")
    else:
        print("Ничья!")


count_players = check_int("Введите кол-во игроков: 2 = 2 игрока, 1 = игрок + бот: ")
if count_players == 2:
    player_1 = input("Введите имя первого игрока: ")
    player_2 = input("Введите имя второго игрока: ")
else:
    player_1 = input("Введите имя игрока: ")
    player_2 = "бот"
player_1, player_2 = lottery(player_1, player_2)
print(f"Первым ходит {player_1}")
game(player_1, player_2)
