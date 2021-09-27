from emoji import emojize
from glob import glob
import logging
from random import randint, choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import settings

from random import randint

logging.basicConfig(filename='bot.log', level=logging.INFO)

# use_context=True - это нужно для того, чтобы перейти со страой библиотеки на новую
# 'переменная'.start_polling() - это регулярные часты обращения за обновлениями/новостми
# 'переменная'.idle() - нужна для того, чтобы бот работал постоянно
# 'переменная'.dispetcher - 
#  CommandHandler - обработчик команд поступающих в телеграмм
# 'переменная'.add.hundler(Comandhundler()) - добавить обработчик
# update.message.reply_text - Ответ пользователю 
# MessageHandler - обработчик, который реагриует на любые сообщения.
# random - генерит случайно число


PROXY = {'proxy_url': settings.proxy_url,
        'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):
    print('Вызови /start')
    context.user_data["emoji"] = get_smile(context.user_data)
    update.message.reply_text(f'Привет, пользователь {context.user_data["emoji"]}!')


def talk_to_me(update, context):
    context.user_data["emoji"] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f'{text} {context.user_data["emoji"]}')
    
def get_smile(user_data):
    if "emoji" not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_dara["emoji"]

def play_random_number(user_number):
    bot_number = randint(user_number -10, user_number+10)
    if bot_number > user_number:
        message = f'Ваше число {user_number}, мое {bot_number}, Вы выиграли'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, мое {bot_number}, ничья'
    else:
        message = f'Ваше число {user_number}, мое {bot_number}, Вы проиграли'
    return message

def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_number(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введите число'
    update.message.reply_text(message)

def send_dog_picture(update, context):
    dog_photo_list = glob('images/dog*.jpg')
    dog_photo_filename = choice(dog_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(dog_photo_filename, 'rb'))

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guees', guess_number))
    dp.add_handler(CommandHandler('dog', send_dog_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__=='__main__':
    main()
