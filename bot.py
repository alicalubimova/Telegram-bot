import telebot
import config
from telebot import types
bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')