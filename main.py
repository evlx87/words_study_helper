# Словари разной сложности
WORDS_EASY = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

WORDS_MEDIUM = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

WORDS_HARD = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

# Ранги пользователя
LEVELS = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

# Словарь для хранения ответов пользователя
answers = {}


def choose_dictionary(difficulty):
    if difficulty == "1" or difficulty == "легкий" or difficulty == "easy":
        return WORDS_EASY
    elif difficulty == "2" or difficulty == "средний" or difficulty == "medium":
        return WORDS_MEDIUM
    elif difficulty == "3" or difficulty == "сложный" or difficulty == "hard":
        return WORDS_HARD
    else:
        return None


print('''Выберите уровень сложности:
1 - Легкий
2 - Средний
3 - Сложный''')
user_select = input("Введите ваш выбор: ").lower()

print(choose_dictionary(user_select))
