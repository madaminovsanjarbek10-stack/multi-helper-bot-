import os
import telebot

# Bot tokenini shu yerga yozasiz (yoki Render muhitidan olingan o'zgaruvchi orqali)
TOKEN = os.getenv('BOT_TOKEN', '8553449044:AAHTUQ_cuGutLiGjOo-RFQA8gmEbh_nLlP4')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men 'Multi Helper' botiman. Sizga qanday yordam bera olaman?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Siz yozdingiz: {message.text}")

print("Bot ishga tushdi...")
bot.infinity_polling()
