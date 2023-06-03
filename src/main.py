import os
import urllib.parse

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import Response
from telebot import types

from src.bot import communication  # noqa
from src.bot import bot

app = FastAPI()


@app.post("/bot/new_update/")
async def new_update(request: Request) -> Response:
    json_body = await request.json()
    update = types.Update.de_json(json_body)
    bot.process_new_updates([update])
    return Response(status_code=200)


@app.on_event("startup")
async def set_webhook() -> None:
    host = os.getenv("PROJECT_HOST")
    url = urllib.parse.urljoin(host, "bot/new_update/")
    bot.set_webhook(url)
