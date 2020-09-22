import telebot
import parser


bot = telebot.TeleBot('980764722:AAHN2MJcRGt8MTyezEL6L0-XvnJT8R8Qau8')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text = message.text
    id_ = message.from_user.id
    if 'привет' in text.lower():
        bot.send_message(id_, "Привет, чем я могу тебе помочь?")
    if 'как дела' in text.lower():
        bot.send_message(id_, "Нормально!")
    if text == 'новости':
        df = parser.main()
        for row in df.iterrows():
            message = row[1]['head'] + '\n'
            message += row[1]['time'] + '\n'
            message += row[1]['tags'] + '\n'
            message += row[1]['url'] + '\n'
            bot.send_message(id_, message)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимать!")
        
        
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)