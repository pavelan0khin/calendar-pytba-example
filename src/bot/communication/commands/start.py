from calendar_pytba import Calendar
from calendar_pytba.utils.types import CalendarLanguage
from telebot import types

from src.bot import bot


@bot.message_handler(commands=["start", "calendar"])
def calendar_command(message: types.Message):
    calendar = Calendar(CalendarLanguage.EN)
    markup = calendar.get_calendar()
    bot.send_message(message.chat.id, "Select date", reply_markup=markup)
