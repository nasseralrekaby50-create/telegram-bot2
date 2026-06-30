import telebot

TOKEN = '8928900432:AAH0DcGm6BAOr_56JBwcmGar6AouUk2640k'  # ضع التوكن الخاص بك هنا

bot = telebot.TeleBot(TOKEN)

# قاموس يحتوي على الرمز والمسار الخاص بالملف المرتبط به
files = {
    "123": "++ wh.cpp",  # ضع مسار ملفك هنا
    # يمكنك إضافة رموز وملفات أخرى بنفس الطريقة
}

@bot.message_handler(func=lambda message: True)
def send_file(message):
    code = message.text.strip()
    
    if code in files:
        file_path = files[code]
        try:
            with open(file_path, "rb") as f:
                bot.send_document(message.chat.id, f)
        except FileNotFoundError:
            bot.reply_to(message, "الملف غير موجود.")
    else:
        bot.reply_to(message, "الرمز غير صحيح.")

bot.polling()
