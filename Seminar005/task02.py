# Задание №2
# Игра с конфетами
# Игроки ходят по очереди, первый ход делает Петя.
# За один ход игрок может съесть не более половины от всех оставшихся конфет, но не менее одной конфеты.
# Игра завершается в тот момент, когда в куче не остается ни одной конфеты.
# Победителем считается игрок, который съел последнюю конфету.

import random


def player_step(player, total) -> list:
    while total > 0:
        step = int(input(f"Ваш шаг {player}! Какое число конфет вы возьмете? - "))
        if total == 1 and step == 1:
            return [player, total]

        elif total / 2 < step or step < 1:
            print(
                f"Вы ввели неправильное число конфет, читайте условие задачи! \nВ вазе по прежнему {total} конфет(ы).")
            continue

        else:
            total -= step
            return [player, total]


def start():
    player = input("Введите ваше имя: ")
    total: int = random.randint(1000, 2001)
    print(f"Всего в вазе {total} конфет(ы)")
    while total > 0:
        player, total = player_step(player, total)
        if total == 0:
            print(f"{player}, вы победитель в этой игре!")
            break

        print(f"В вазе осталось {total} конфет(ы)")
        if total == 1:
            print("Бот Василёк забирает последнюю конфету и побеждает в игре!")
            break

        bot_step = random.randint(1, total // 2)
        total -= bot_step
        print(f"Бот Васёк взял {bot_step} конфет(ы). Итого в вазе {total} конфет(ы)")


start()
