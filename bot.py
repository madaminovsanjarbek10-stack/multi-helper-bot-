import os
import telebot
from openai import OpenAI

BOT_TOKEN = os.getenv('BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

bot = telebot.TeleBot(BOT_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men hamma savollaringizga javob bera oladigan va sizga yordam beradigan sun'iy intellekt botiman. Menga istalgan savolni bering!")

@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Siz yordamchi va aqlli sun'iy intellekt botisiz. Barcha savollarga o'zbek tilida aniq va foydali javob bering."},
                {"role": "user", "content": message.text}
            ]
        )
        answer = response.choices[0].message.content
        bot.reply_to(message, answer)
    except Exception as e:
        bot.reply_to(message, f"Kechirasiz, xatolik yuz berdi: {str(e)}")

print("Sun'iy intellekt bot ishga tushdi...")
bot.infinity_polling()
