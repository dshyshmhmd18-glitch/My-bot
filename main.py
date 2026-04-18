import telebot
import os
from threading import Thread
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "البوت شغال الآن! 🎫"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

API_TOKEN = '8714501250:AAFHPTPrruC049lJihl41RwdGpOxwEmrOao'
MY_CHAT_ID = 7023033626

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك في نظام التسجيل! 🎫\n\nأرسل صورة التشكيلة الآن.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    user = message.from_user
    caption = f"🎫 تشكيلة جديدة من: {user.first_name}\n🆔: {user.id}"
    bot.send_photo(MY_CHAT_ID, message.photo[-1].file_id, caption=caption)
    bot.reply_to(message, "تم استلام صورة تشكيلتك بنجاح! 🎫")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.reply_to(message, "من فضلك أرسل صورة التشكيلة 🎫")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
  
