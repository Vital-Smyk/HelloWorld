from re import template
import telebot
from const import BOT_TOKEN
from pars import get_parsed_data
from bot_keyb import get_main_kb

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.from_user.id,
        text='''
        Привет! Я твой погодный бот! <(^_^)>
        ''',reply_markup=get_main_kb(),
    )

@bot.message_handler(content_types= ['text'])
def main_message_handler(message):
    if message.text == 'Cегодня' :
        temperature, description = get_parsed_data()
        if temperature is not None and description is not None:
            bot.send_message(
            message.from_user.id,
            text=f'''  (⊃｡•́‿•̀｡)⊃  \nСегодня температура в Херсоне: {temperature} \nПрогноз: {description}
            ''')
        else :
             bot.send_message(
                message.from_user.id,
                text='''
                Невозможно получить данные!
                ''')
    elif message.text == 'Спасибо' :
        bot.send_message(
            message.from_user.id,
            text=''' <(UwU)> \nНе нужно благодарностей!...Хотя нет ... Хвали меня!
              ''',    
            )
if __name__ == '__main__':
    bot.polling(non_stop=True)