from telegram.ext import Updater, CommandHandler, messagehandler
import logging

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = "به ربات قیمت ارز خوش آمدید. \n برای مطلع شدن از قیمت ارز آن را تایپ کنید")

def طلا(update, context):
    # read the info from online api
    gold_price = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=" تومان"+price+"قیمت طلا: ")

def سکه(update, context):
    price = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=" تومان"+price+"قیمت سکه: ")

def دلار(update, context):
    price = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=" تومان"+price+"قیمت دلار: ")

def پوند(update, context):
    price = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=" تومان"+price+"قیمت پوند: ")

def یورو(update, context):
    price = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=" تومان"+price+"قیمت یورو: ")

def لیر(update, context):
    price = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=" تومان"+price+"قیمت لیر: ")

def بیت_کوین(update, context):
    price = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=" دلار"+price+"قیمت بیت کوین: ")

def اتریوم(update, context):
    price = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=" دلار"+price+"قیمت اتریوم: ")

# getting token from file
token_file = open("token.txt", "r")
tok = token_file.read()

updater = Updater(token=tok, use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

dispatcher = updater.dispatcher

strat_handler = CommandHandler('start', start)
dispatcher.add_handler(strat_handler)

updater.start_polling()


