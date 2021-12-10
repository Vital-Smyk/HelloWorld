from re import template
import telebot
from const import BOT_TOKEN
from pars import get_today_data, get_week_data
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
    if message.text == 'На сегодня' :
        temperature, description = get_today_data()
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
    
    elif message.text == 'На неделю' :
        d1,ds1,d2,ds2,d3,ds3,d4,ds4,d5,ds5,d6,ds6,d7,ds7 = get_week_data()
        if  d1 is not None and ds1 is not None:
            bot.send_message(
            message.from_user.id,
            text=f'''  (⊃｡•́‿•̀｡)⊃  \nТаков прогноз погоды на неделю:
            {d1}\nПрогноз: {ds1}\n
            {d2}\nПрогноз: {ds2}\n
            {d3}\nПрогноз: {ds3}\n
            {d4}\nПрогноз: {ds4}\n
            {d5}\nПрогноз: {ds5}\n
            {d6}\nПрогноз: {ds6}\n
            {d7}\nПрогноз: {ds7}\n
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
            text='''<(UwU)> \nНе нужно благодарностей!...Хотя нет ... Хвали меня!''',)


if __name__ == '__main__':
    bot.polling(non_stop=True)