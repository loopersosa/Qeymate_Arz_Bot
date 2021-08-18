from telegram.ext import Updater, CommandHandler, messagehandler
import logging

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = "به ربات قیمت ارز خوش آمدید. \n برای مطلع شدن از قیمت ارز آن را تایپ کنید")
#def help(update )
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

gold_price_handler = CommandHandler("طلا", طلا)
dispatcher.add_handler(gold_price_handler)

coin_price_handler = CommandHandler("سکه", سکه)
dispatcher.add_handler(coin_price_handler)

dollar_price_handler = CommandHandler("دلار", دلار)
dispatcher.add_handler(dollar_price_handler)

euro_price_handler = CommandHandler("یورو", یورو)
dispatcher.add_handler(euro_price_handler)

pound_price_handler = CommandHandler("پوند", پوند)
dispatcher.add_handler(pound_price_handler)

lire_price_handler = CommandHandler("لیر", لیر)
dispatcher.add_handler(lire_price_handler)

bitcoin_price_handler = CommandHandler("بیت کوین", بیت_کوین)
dispatcher.add_handler(bitcoin_price_handler)

etherium_price_handler = CommandHandler("اتریوم", اتریوم)
dispatcher.add_handler(etherium_price_handler)

updater.start_polling()
