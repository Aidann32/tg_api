from django.conf import settings

import telebot
from rest_framework.authtoken.models import Token


bot = telebot.TeleBot(settings.TELEGRAM_TOKEN, parse_mode=None)
if settings.DEBUG:
    host = settings.NGROK_HOST
else:
    host = settings.HOST

webhook_url = f'https://{host}/bot/{settings.TELEGRAM_TOKEN}/webhook/'


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Hello! Send me auth_token generated after registration")

@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id, "This bot accepts only tokens," +
        " if you want to link token with your API user send auth_token generated after registration in API")

@bot.message_handler(content_types='text')
def message_reply(message):
    if Token.objects.filter(key=message.text).exists():
        user = Token.objects.get(key=message.text).user    
        user.chat_id = message.chat.id 
        user.save()
        bot.send_message(message.chat.id, 'Your API user successfully linked to this chat!')
    else:
        bot.send_message(message.chat.id, 'This token does not exist in database!')


bot.remove_webhook()
bot.set_webhook(url=webhook_url)


