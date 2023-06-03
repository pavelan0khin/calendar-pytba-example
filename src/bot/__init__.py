import os

from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()


api_token = os.getenv("TELEGRAM_BOT_TOKEN")

bot = TeleBot(api_token)
