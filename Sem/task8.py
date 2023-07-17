# ✔ Создайте пакет с всеми модулями, которые вы
# создали за время занятия.
# ✔ Добавьте в __init__ пакета имена модулей внутри
# дандер __all__.
# ✔ В модулях создайте дандер __all__ и укажите только
# те функции, которые могут верно работать за
# пределами модуля.


from sem_6 import guess, riddle_game, get_circle_riddles_1, get_circle_riddles_2, show_results, check_date, check_year


print(guess(10, 100, 9))
print()


question = "Сидит дед в сто шуб одет, кто его раздевет, тот слёзы проливает"
answers_ = ['лук', 'onion']
result = riddle_game(question, answers_, 3)
print(f"Вы угадали с {result} попытки" if result != 0 else "Вы не угадали")
print()


riddles_ = {"Сидит дед в сто шуб одет, кто его раздевет, тот слёзы проливает": ['лук', 'onion'],
                "Висит груша нельзя скушать": ["лампочка", "лампа", "light bulb"]}
get_circle_riddles_1(riddles_)
print()


riddles_ = {"Сидит дед в сто шуб одет, кто его раздевет, тот слёзы проливает": ['лук', 'onion'],
                "Висит груша нельзя скушать": ["лампочка", "лампа", "light bulb"]}
get_circle_riddles_2(riddles_)
show_results()
print()


print(check_date("22.11.1980"))
print(check_year("14.11.1980"))
