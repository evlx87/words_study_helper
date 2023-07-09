"""Программа помощник для изучения английских слов"""
# Словари разной сложности
WORDS_EASY = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута"}

WORDS_MEDIUM = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать"}

WORDS_HARD = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме"}

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
    """Функция для выбора сложности"""
    difficulty_mapping = {
        "1": WORDS_EASY, "легкий": WORDS_EASY, "easy": WORDS_EASY,
        "2": WORDS_MEDIUM, "средний": WORDS_MEDIUM, "medium": WORDS_MEDIUM,
        "3": WORDS_HARD, "сложный": WORDS_HARD, "hard": WORDS_HARD
    }
    return difficulty_mapping.get(difficulty)


print('''Выберите уровень сложности:
1 - Легкий
2 - Средний
3 - Сложный''')
user_select = input("Введите ваш выбор: ").lower()

words = choose_dictionary(user_select)
