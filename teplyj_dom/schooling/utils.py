# from telegram import Bot
from django.conf import settings

# bot = Bot(token=settings.BOT_TOKEN)


async def send_telegram_message(**kwargs):
    """
    Отправка сообщения в группу организации от имени телеграм-бота.

    Вывод сообщения об отправителе:
    - name: Имя пользователя
    - phone: Телефон пользователя
    - email: Электронная почта пользователя
    - text: Текст обращения пользователя
    """
    name = kwargs.get('name')
    phone = kwargs.get('phone')
    email = kwargs.get('email')
    text = kwargs.get('text')
    message = (
        'Новый запрос от пользователя. \n\n'
        f'Имя: {name} \n'
        'Контактные данные \n'
        f' - телефон: {phone} \n'
        f' - почта: {email} \n\n'
        'Текст обращения: \n'
        f'{text}'
    )
    await bot.send_message(
        chat_id=settings.CHANNEL_ID,
        text=message
    )
