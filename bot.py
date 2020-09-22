import telebot


bot = telebot.TeleBot('980764722:AAHN2MJcRGt8MTyezEL6L0-XvnJT8R8Qau8')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == 'Как дела?':
        bot.send_message(message.from_user.id, "Нормально!")
    else:
        bot.send_message(message.from_user.id, "lolkek")
        
        
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)