
import telebot
from telebot import types

token = 'TOKEN'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Расскажи о себе!', 'Как с тобой связаться?', '')
    keyboard.row('Как найти тебя в соц.сетях?')
    bot.send_message(message.chat.id, 'Здравствуйте! Я - Дима Артёменко.', reply_markup=keyboard)
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'расскажи о себе!':
            bot.send_message(message.chat.id, 'Я - просто школьник из Новочеркасска:) Зовут Димой Артёменко. Ну или же просто Артём. Вместе со своей командой увлекаюсь кодингом) Пишу на много чём, но мой основное направление - WEB-разработка. Мне 13 и в свой возраст - я просто нарабатываю портфолио!')
        if message.text.lower() == 'как с тобой связаться?':
            bot.send_message(message.chat.id, 'Очень просто:) Я всегда открыт для общения! Пишите @Suicidessss')
        if message.text.lower() == 'как найти тебя в соц.сетях?':
            bot.send_message(message.chat.id, 'Instagram: @a.r.t.i.k_dimovich VK: @rioar Telegram: @Suicidessss')
bot.polling()
