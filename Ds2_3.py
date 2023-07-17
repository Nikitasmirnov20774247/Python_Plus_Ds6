# Задача 2
# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка
# 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Задача 3
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.


from random import randint as rd
from Sem.sem_6 import check_chessboard


def get_chessboard():
    chessboard = []

    for x in range(1, 9):
        line = []
        y = rd(1, 8)
        for i in range(1, 9):
            if i != y:
                line.append(0)
            else:
                line.append(1)
        chessboard.append(line)
    return chessboard


def print_chessboard(chessboard):
    for i in chessboard:
        print(i)


if __name__ == '__main__':
    count = 1
    for i in range(4):
        check = False
        while check == False:
            chessboard = get_chessboard()
            check = check_chessboard(chessboard)
            count += 1
        print(f'Попытка №{count}')
        print_chessboard(chessboard)
