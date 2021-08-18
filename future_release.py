from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token=input("enter your token here: "))
dispatcher = updater.dispatcher


def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="send the name of a currency to get its price")


def main(update, context):
    message = update.message.text
    if message == "ethereum":
        context.bot.send_message(chat_id=update.effective_chat.id, text=ethereum())
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="no currency with this name found")


def ethereum():
    """ this command gets the price of ethereum from API and returns it """
    return "api call not implemented yet"


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
main_handler = MessageHandler(~Filters.command, main)
dispatcher.add_handler(main_handler)


if __name__ == "__main__":
    updater.start_polling()

