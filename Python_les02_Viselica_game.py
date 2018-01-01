# coding: utf-8
import random

MAX_ERRORS = 8
cyrillic = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЪЭЮЯ"
error_counter = 0
letters_used = []
restart_answer = "1"

# Подгрузка словаря из файла
with open("words.txt", "r") as f:
    words_list = f.read().upper().split("\n")

# Информирование о размере словаря
print(f"В базе игры содержится {len(words_list)} cлов.")

# Загаданное слово
secret_word = random.sample(words_list, 1)[0]
#print(secret_word)  # отладочный параметр

# Строка-загадка со спецсимволом
game_word = ["*"] * len(secret_word)
print("".join(game_word))


while True:
    while restart_answer in ["1", "2"]:
        letter = input("Введите букву: ").upper()
        if len(letter) != 1 or letter not in cyrillic:
            print("Следует использовать только символы русской клавиатуры!")
            continue

        if letter in letters_used:
            print(f"Буква '{letter}' уже была...")
            continue

        # Ввод верной буквы
        if letter in secret_word:
            print(f"Буква '{letter}' есть в загаданном слове!")
            for w_index, char in enumerate(secret_word):
                if char == letter:
                    game_word[w_index] = letter

        # Ввод неверной буквы
        else:
            error_counter += 1
            letters_used.append(letter)
            print(f"Нет буквы '{letter}' в загаданном слове, ошибок {error_counter}/{MAX_ERRORS}.")

        print("".join(game_word))

        # Условие проигрыша
        if error_counter == MAX_ERRORS:
            print(f"\nВы ошиблись максимальное количество раз, поэтому Вы выиграли! :(")
            print("Хотите сыграть ещё раз? (Y/N) :")
            print("[1] Да")
            print("[2] Нет")
            restart_answer = input("Ваш выбор: ")
            if restart_answer == "1":
                error_counter = 0
                letters_used = [""]
                secret_word = random.sample(words_list, 1)[0]
                game_word = ["*"] * len(secret_word)
                print(f"Загадано новое слово! Количество буквы: {len(secret_word)}")
                continue  # что лучше continue или pass?
            if restart_answer == "2":
                print("Пока..")
                exit(0)

        # Условие победы
        if "*" not in game_word:
            print(f"Поздравляем, Вы угадали слово '{secret_word}'!")
            print("Хотите сыграть ещё раз?")
            print("[1] Да")
            print("[2] Нет")
            restart_answer = input("Ваш выбор: ")
            if restart_answer == "1":
                error_counter = 0
                letters_used = [""]
                secret_word = random.sample(words_list, 1)[0]
                game_word = ["*"] * len(secret_word)
                print(f"Загадано новое слово! Количество буквы: {len(secret_word)}")
                continue  # что лучше continue или pass?
            if restart_answer == "2":
                print("Пока..")
                exit(0)

    while restart_answer not in ["1", "2"]:
        print("Неизвестное значение. Выберите значение [1] или [2]")
        restart_answer = input(": ")
        if restart_answer == "1":
            error_counter = 0
            letters_used = [""]
            secret_word = random.sample(words_list, 1)[0]
            game_word = ["*"] * len(secret_word)
            print(f"Загадано новое слово! Количество буквы: {len(secret_word)}")
            continue # что лучше continue или pass?
        if restart_answer == "2":
            print("Пока..")
            exit(0)

print("Пока..")