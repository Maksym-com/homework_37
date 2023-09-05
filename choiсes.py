from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Текст вибору 1
en_choice = {'en' : "Find a movie by genre🎭", 'en1' : "Find a random movie🎲", 'en2' : "Find a movie by title🤙"}
uk_choice = {'uk' : "Знайдіть фільм за жанром🎭", 'uk1' : "Знайдіть випадковий фільм🎲", 'uk2' : "Знайдіть фільм за назвою🤙"}
it_choice = {'it' : "Trova un film per genere🎭", 'it1' : "Trova un film a caso🎲", 'it2' : "Trova il film per titolo🤙"}


# Створення клавіатури вибору 1
# english
def dynamic_en_choice():
    inline_keyboard = InlineKeyboardMarkup()
    for genre, label in en_choice.items():
        button = InlineKeyboardButton(text=label, callback_data=genre)
        inline_keyboard.add(button)
    return inline_keyboard
# ukrainian
def dynamic_uk_choice():
    inline_keyboard = InlineKeyboardMarkup()
    for genre, label in uk_choice.items():
        button = InlineKeyboardButton(text=label, callback_data=genre)
        inline_keyboard.add(button)
    return inline_keyboard
# italian
def dynamic_it_choice():
    inline_keyboard = InlineKeyboardMarkup()
    for genre, label in it_choice.items():
        button = InlineKeyboardButton(text=label, callback_data=genre)
        inline_keyboard.add(button)
    return inline_keyboard

# Вибір фільмів за жанром 
genre_list_en = {
        'drama' : "Drama😕",
        'thriller' : "Thriller🔫",
        'romance' : "Romance🤍",
        'crime' : "Crime🗄",
        'adventure' : "Adventure🤯",
        'fantasy' : "Fantasy🦄",
        'science_fiction' : "Science Fiction👽",
        'animation' : "Animation😇",
        'western' : "Western🤠🐴",
        'war_politics' : "War & Politics♟",
        'comedy' : "Comedy🤣",
        'action' : "Action💥",
        'horror' : "Horror😱",
        'documentary' : "Documentary📑",
        'mystery' : "Mystery🧐",
        'family' : "Family👨‍👩‍👧‍👦",
        'history' : "History🤔",
        'kids' : "Kids👶👧"
}
 
genre_list_uk = {
        'drama' : "Драма😕",
        'thriller' : "Трилер🔫",
        'romance' : "Романтичний🤍",
        'crime' : "Кримінал🗄",
        'adventure' : "Пригоди🤯",
        'fantasy' : "Фентезі🦄",
        'science_fiction' : "Наукова фантастика👽",
        'animation' : "Анімаційний😇",
        'western' : "Вестерн🤠🐴",
        'war_politics' : "Війна і Політика♟",
        'comedy' : "Комедія🤣",
        'action' : "Бойовик💥",
        'horror' : "Жахи😱",
        'documentary' : "Документальний📑",
        'mystery' : "Загадка / Детектив🧐",
        'family' : "Сімейний👨‍👩‍👧‍👦",
        'history' : "Історичний🤔",
        'kids' : "Дитячий👶👧"
}

genre_list_it = {
        'drama' : "Drammatico😕.",
        'thriller' : "Thriller🔫.",
        'romance' : "Romance🤍.",
        'crime' : "Crime🗄.",
        'adventure' : "Avventura🤯.",
        'fantasy' : "Fantasy🦄.",
        'science_fiction' : "Fantascienza👽.",
        'animation' : "Animazione😇.",
        'western' : "Western🤠🐴.",
        'war_politics' : "Guerra e Politica♟.",
        'comedy' : "Commedia🤣.",
        'action' : "Azione💥.",
        'horror' : "Horror😱.",
        'documentary' : "Documentario📑.",
        'mystery' : "Misterio🧐.",
        'family' : "Famiglia👨‍👩‍👧‍👦.",
        'history' : "Storia🤔.",
        'kids' : "bambini👶👧."
}

# Cтворення клавіатур за жанром (тут чат gpt поміг)
# Жанри англійською
def dynamic_inline_kb_en():
    inline_keyboard = InlineKeyboardMarkup()
    row_buttons = []  # Створити список для кнопок у поточному рядку

    for genre, label in genre_list_en.items():
        button = InlineKeyboardButton(text=label, callback_data=genre)
        row_buttons.append(button)  # Додати кнопку до поточного рядку

        # Якщо набралося дві кнопки в поточному рядку
        if len(row_buttons) == 2:
            inline_keyboard.row(*row_buttons)  # Додати рядок до клавіатури
            row_buttons = []  # Очистити список для наступного рядку

    return inline_keyboard
# Жанри українською
def dynamic_inline_kb_uk():
    inline_keyboard = InlineKeyboardMarkup()
    row_buttons = []  # Створити список для кнопок у поточному рядку

    for genre, label in genre_list_uk.items():
        button = InlineKeyboardButton(text=label, callback_data=genre)
        row_buttons.append(button)  # Додати кнопку до поточного рядку

        # Якщо набралося дві кнопки в поточному рядку
        if len(row_buttons) == 2:
            inline_keyboard.row(*row_buttons)  # Додати рядок до клавіатури
            row_buttons = []  # Очистити список для наступного рядку

    return inline_keyboard
# Жанри італійською
def dynamic_inline_kb_it():
    inline_keyboard = InlineKeyboardMarkup()
    row_buttons = []  # Створити список для кнопок у поточному рядку

    for genre, label in genre_list_it.items():
        button = InlineKeyboardButton(text=label, callback_data=genre)
        row_buttons.append(button)  # Додати кнопку до поточного рядку

        # Якщо набралося дві кнопки в поточному рядку
        if len(row_buttons) == 2:
            inline_keyboard.row(*row_buttons)  # Додати рядок до клавіатури
            row_buttons = []  # Очистити список для наступного рядку

    return inline_keyboard