import telebot
bot = telebot.TeleBot('7261075250:AAGkGKmU8rDgW8szsd93PUVSUDt0YGdB68M')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я Duo!\nЧем я могу тебе помочь?\nНапиши /help и узнаешь все команды!")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "/stat English":
        bot.send_message(message.from_user.id, "Пройдено модулей - 2\nМаксимум уроков за один день - 4\nМаксимальная Лига - Серебряная\nИзучено слов -204\nМаксимальный ударный режим - 19")
    elif message.text == '/stat German':
        bot.send_message(message.from_user.id, "Извини, но ты ещё не начал изучение этого языка")
    elif message.text == '/info Logrot':
        bot.send_message(message.from_user.id, "АНТОН КАКОРИН антропоморф")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)