"""Программа помощник для изучения английских слов"""
import random

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
    """Функция для выбора сложности и выбора словаря"""
    difficulty_mapping = {
        "1": WORDS_EASY, "легкий": WORDS_EASY, "easy": WORDS_EASY,
        "2": WORDS_MEDIUM, "средний": WORDS_MEDIUM, "medium": WORDS_MEDIUM,
        "3": WORDS_HARD, "сложный": WORDS_HARD, "hard": WORDS_HARD
    }
    return difficulty_mapping.get(difficulty)


def choose_word(iterator):
    """Получаем слово из словаря, его перевод, длину и первую букву"""
    word, word_translate = next(iterator)
    word_length = len(word)
    word_first_letter = word_translate[0]
    question_string = f"{word.capitalize()}, {word_length} букв, начинается на {word_first_letter}..."
    return question_string, word_translate, word


def question_answer(dictionary):
    """Вывод вопроса и получения ответа"""
    iterator = iter(dictionary.items())
    for _ in dictionary:
        question_string, word_translate, word = choose_word(iterator)
        print(question_string)
        user_answer = input("Введите ваш ответ: ").lower()
        if user_answer == word_translate:
            print(f"Верно. {word.capitalize()} - это {word_translate}")
            answers[word] = True
        else:
            print(f"Неверно. {word.capitalize()} - это {word_translate}")
            answers[word] = False


def result_output(answers_dictionary):
    """Вывод результата"""
    answers_true = [word for word, value in answers_dictionary.items() if value]
    answers_false = [word for word, value in answers_dictionary.items() if not value]
    # Выдаем пользователю список верных/неверных ответов
    print("Правильно отвечены слова:")
    for word in answers_true:
        print(word)
    print("\nНеправильно отвечены слова:")
    for word in answers_false:
        print(word)
    # Высчитываем ранг пользователя
    user_result = len(answers_true)
    print(f"\nВаш ранг:\n{LEVELS[user_result]}")


# Запрашиваем у пользователя уровень сложности и выбираем нужный словарь
print('''Выберите уровень сложности:
1 - Легкий
2 - Средний
3 - Сложный''')
user_select = input("Введите ваш выбор: ").lower()

words = choose_dictionary(user_select)

question_answer(words)

result_output(answers)
