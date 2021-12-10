from typing import Text
import telebot

def get_main_kb():
    todays_temperature_btn = telebot.types.KeyboardButton(text='Cегодня')
    thnks_btn = telebot.types.KeyboardButton(text='Спасибо')
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.row(todays_temperature_btn,thnks_btn)
    return keyboard