from calendar_pytba.utils.handler import callback_handler
from calendar_pytba.utils.types import CalendarLanguage

from src.bot import bot
from src.bot.communication.callbacks import selected_date


callback_handler(bot, CalendarLanguage.EN)
