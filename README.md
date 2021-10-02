# Проект DogBot

DogBot - это бот для Telegram, который присылает пользователю картинки собачек.

## Установка 

1. Клинируйте репозиторий с github
2. Создайте виртуальное окружение
3. Установите зависимости `pip install -r requerements.txt`
4. Cоздайте файл `settings.py`, в котором будут настройки 
5. Впишите в settings.py переменные : 
```
API_KEY = 'Api телеграм ключ, который дает Botfather'
proxy_url = 'Адрес прокси'
PROXY_USERNAME = 'Логин прокси'
PROXY_PASSWORD = 'Пароль прокси'
USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:',':earth_asia:', ':tada:']
```
6. Заупстите бота командой `python Mybot.py`