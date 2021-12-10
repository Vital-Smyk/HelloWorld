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
        temperature, description = get_today_data
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
        d1,d2,d3,d4,d5,d6,d7,des1,des2,des3,des4,des5,des6,des7 = get_week_data()
        if  d1 is not None and des1 is not None:
            bot.send_message(
            message.from_user.id,
            text=f'''  (⊃｡•́‿•̀｡)⊃  \nТаков прогноз погоды на неделю:
            {d1}\nПрогноз:{des1}
            {d2}\nПрогноз:{des2}
            {d3}\nПрогноз:{des3}
            {d4}\nПрогноз:{des4}
            {d5}\nПрогноз:{des5}
            {d6}\nПрогноз:{des6}
            {d7}\nПрогноз:{des7}
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