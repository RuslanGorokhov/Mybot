import settings
from emoji import emojize
from random import randint, choice
from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_smile(user_data):
    if "emoji" not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data["emoji"]

def play_random_number(user_number):
    bot_number = randint(user_number -10, user_number+10)
    if bot_number > user_number:
        message = f'Ваше число {user_number}, мое {bot_number}, Вы выиграли'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, мое {bot_number}, ничья'
    else:
        message = f'Ваше число {user_number}, мое {bot_number}, Вы проиграли'
    return message


def main_keyboard():
    return ReplyKeyboardMarkup([['Прислать собачку','Test', KeyboardButton('Мои координаты', request_location=True)]])

