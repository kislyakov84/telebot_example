import telebot
from telebot import types

token = '2054413344:AAFTX1Z0I-GB9v1JfwVgQtT4zc6U4SU4U4g'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, "Привет я тестовый бот ")

@bot.message_handler(commands=['button'])
def button_message(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Кнопка")
	markup.add(item1)
	bot.send_message(message.chat.id, "Выберите что вам нужно", reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
	if message.text=="Кнопка":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Кнопка 2")
		markup.add(item1)
		bot.send_message(message.chat.id, "Выберите что вам нужно", reply_markup=markup)
	elif message.text=="Кнопка 2":
		bot.send_message(message.chat.id, "Спасибо за чтение статьи!")

bot.infinity_polling()