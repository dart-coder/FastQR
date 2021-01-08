from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
from os import remove, system
from re import match
from json import load


def start(update, context):
    CHAT_ID = update.effective_chat.id
    USER = update.message.from_user
    STICKER = open("greeting_sticker.tgs", "rb")
    TEXT = open("greeting.txt", encoding="utf-8").read().format(USER.first_name)
    context.bot.send_animation(chat_id=CHAT_ID, animation=STICKER)
    context.bot.send_message(chat_id=CHAT_ID, text=TEXT, parse_mode=ParseMode.MARKDOWN)


def make_qr(url: str):
    PATTERN = open("pattern.txt", encoding="utf-8").read()
    if len(url) <= 300 and match(PATTERN, url):
        system(f"myqr {url} -n qr_code.png")


def send_qr(update, context):
    CHAT_ID = update.effective_chat.id
    url = update.message.text
    make_qr(url)
    try:
        context.bot.send_photo(chat_id=CHAT_ID, photo=open("qr_code.png", "rb"))
        remove("qr_code.png")
    except:
        context.bot.send_message(chat_id=CHAT_ID, text="Некорректный URL!")
    

if __name__ == "__main__":
    with open("config.json", encoding="utf-8") as file:
        TOKEN = load(file)["TOKEN"]
    
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, send_qr))
    updater.start_polling()
