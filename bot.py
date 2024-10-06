import telebot

token = '7225255703:AAE5WkXtFqxOBNXRRU6XhxKvYVLU0l5f3s4'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "bot now working")
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    #bot.send_message(message.chat.id,message.text)
    bot.reply_to(message,message.text)
bot.infinity_polling()