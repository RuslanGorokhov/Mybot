from glob import glob
from random import choice
from untils import get_smile, play_random_number, main_keyboard

def greet_user(update, context):
    print('Вызови /start')
    context.user_data["emoji"] = get_smile(context.user_data)
    update.message.reply_text(
        f'Привет, пользователь {context.user_data["emoji"]}!',
         reply_markup=main_keyboard()
    )


def talk_to_me(update, context):
    context.user_data["emoji"] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f'{text} {context.user_data["emoji"]}')
    

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
    update.message.reply_text(message, reply_markup=main_keyboard())


def send_dog_picture(update, context):
    dog_photo_list = glob('images/dog*.jpg')
    dog_photo_filename = choice(dog_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(dog_photo_filename, 'rb'), reply_markup=main_keyboard())   

def user_coordinats(update, context):
    context.user_data["emoji"] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f'Ваши координаты {coords} {context.user_data ["emoji"]}!',
        )