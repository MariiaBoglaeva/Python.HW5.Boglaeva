# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# Игра для двух игроков и бота
import random


def check_int(question=str): #проверка на ввод числа
    data = input(question)
    while ((not data.isdigit()) or int(data) == 0):
        data = input(f"Ошибка ввода!\n {question}")
    return int(data)


type_game = check_int("Выберете формат игры: 1 = два игрока, 2 = игрок и бот:")
if type_game == 1:
    player_1 = input("Введите имя первого игрока: ")
    player_2 = input("Введите имя второго игрока: ")
else:
    player_1 = input("Введите имя игрока: ")
    player_2 = "бот"
count_candy = check_int("Задайте кол-во конфет: ")


def lottery(name_1, name_2):
    lottery_num = random.randint(1, 2)
    if lottery_num != 1:
        name_1, name_2 = name_2, name_1
    return (name_1, name_2)


player_1, player_2 = lottery(player_1, player_2)

print(f"Первым ходит {player_1}")


def game(count, name_1, name_2, max_count=28):
    flag = True
    name = name_1
    while count > 0:
        if flag:
            name = name_1
        else:
            name = name_2
        if name != "бот":
            q = f"{name}, сколько берешь конфет: "
            step = check_int(q)
        else:
            # обычный бот:

            # if count > max_count:
            #    step = random.randint(1, max_count)
            # else:
            #    step = random.randint(1, count)

            # бот с интеллектом:
            if count > max_count:
                step = count % (max_count + 1)
                if step == 0:
                    step = max_count
            else:
                step = count
        if step <= max_count and step <= count:
            count -= step
            flag = not flag
            print(f"{name} взял {step} конфет, осталось {count}")
        elif step > max_count and count > max_count:
            print(f"За ход можно взять не более {max_count} конфет!")
        else:
            print(f"Можно взять не более {count} конфет!")
    return (step, name)


remainder, winner = game(count_candy, name_1=player_1, name_2=player_2)
print(f"Победил {winner}, забрав последние {remainder} конфет!")
