# Задача 1
# В модуль с проверкой даты  добавьте возможность запуска в терминале с передачей даты на проверку.


from sys import argv
from Sem.sem_6 import check_date


if __name__ == '__main__':
    if len(argv) > 1:
        if check_date(argv[1]):
            print("Дата корректна")
        else:
            print("Дата некорректна")
    else:
        print("!! Вы не ввели дату !!")
