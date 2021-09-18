import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

# use_context=True - это нужно для того, чтобы перейти со страой библиотеки на новую
# 'переменная'.start_polling() - это регулярные часты обращения за обновлениями/новостми
# 'переменная'.idle() - нужна для того, чтобы бот работал постоянно
# 'переменная'.dispetcher - 
#  CommandHandler - обработчик команд поступающих в телеграмм
# 'переменная'.add.hundler(Comandhundler()) - добавить обработчик
# update.message.reply_text - Ответ пользователю 
# MessageHandler - обработчик, который реагриует на любые сообщения.

PROXY = {'proxy_url': settings.proxy_url,
        'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):
    print('Вызови /start')
    update.message.reply_text('Привет,  пользователь! Ты вызвал команду /start')


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__=='__main__':
    main()
