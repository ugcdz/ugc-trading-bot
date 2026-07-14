import os
import telebot
from flask import Flask, request

# إعداد توكن البوت والـ Chat ID الخاص بك يا رمزي
BOT_TOKEN = "8679771348:AAGWxmgWLwQLdUjGDlt6iYvS4BGpw08grzg"
CHAT_ID = "8479316709"

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "البوت يعمل بنجاح 24/7!"

# استقبال التنبيهات من TradingView وإرسالها لك فوراً
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        # استخراج الرسالة القادمة من التنبيه
        message = data.get('text', '🚨 تنبيه تداول جديد تم تفعيله!')
        
        # إرسال الرسالة إلى حسابك في تلغرام
        bot.send_message(CHAT_ID, message)
        return {"status": "success"}, 200
    except Exception as e:
        print("Error:", e)
        return {"status": "error"}, 400

if __name__ == "__main__":
    # تشغيل السيرفر
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
