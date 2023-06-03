import datetime

from calendar_pytba.utils.types import CallBackData
from telebot import types

from src.bot import bot


@bot.callback_query_handler(
    func=lambda call: call.data.startswith(CallBackData.SELECTED_DATE)
)
def selected_date_call(call: types.CallbackQuery) -> None:
    date_as_string = call.data.split(":")[1]
    date = datetime.datetime.strptime(date_as_string, "%Y-%m-%d")
    answer_text = f"Your date is {date.strftime('%d.%m.%Y')}"
    bot.answer_callback_query(call.id, answer_text, True)
