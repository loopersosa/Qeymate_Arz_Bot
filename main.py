# let's write this code in 2 versions: 1. Eng 2. Per ... Ok


from telegram.ext.picklepersistence import PicklePersistence
import functions, logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler


def main(update, context):
    message = update.message.text.lower()
    if not context.user_data.get("lang", None):
        # if the user has not chose a language yet:
        context.bot.send_message(chat_id=update.effective_chat.id, text="please choose your language first")
        functions.start(update, context)  # the start function will enable the user to choose a language
        return  # to stop running this function
    lang = context.user_data.get("lang", None)

    if ("ethereum" in message) or ("اتریوم" in message):
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.ethereum(lang))
    elif ("bitcoin" in message) or ("بیت کوین" in message):
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.bitcoin(lang))
    elif ("coin" in message) or ("سکه" in message):
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.coin(lang))
    elif ("dollar" in message) or ("دلار" in message):
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.dollar(lang))
    elif ("euro" in message) or ("یورو" in message):
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.euro(lang))
    elif ("gold" in message) or ("طلا" in message):
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.gold(lang))
    elif ("pound" in message) or ("پوند" in message):
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.pound(lang))
    elif ("lire" in message) or ("لیر" in message):
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.lire(lang))
    else:
        if lang == "en":
            context.bot.send_message(chat_id=update.effective_chat.id, text="no currency with this name found\
                                                                             \nlist of currencies: /help")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="هیچ ارزی با این نام پیدا نشد\n \
                                                                             لیست ارز ها: /help")


# commands
start_handler = CommandHandler(['start', 'Start'], functions.start)
help_handler = CommandHandler(['Help', 'help'], functions.help)

# choose language
lang_handler = CallbackQueryHandler(functions.lang)

# messages
main_handler = MessageHandler(Filters.text & ~Filters.command, main)
unsupported_message = MessageHandler((~Filters.text) & (~Filters.command), functions.help)



if __name__ == "__main__":
    # getting token from file
    with open("token.txt", "rt") as token_file:
        tok = token_file.read()

    # the following will save users' data in a
    # file named "users_data.dat" so that we don't
    # lose our data after restarting the bot:
    persistence = PicklePersistence(filename="users_data.dat")
    updater = Updater(token=tok, persistence=persistence)
    updater.start_polling()
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(lang_handler)
    dispatcher.add_handler(main_handler)
    dispatcher.add_handler(unsupported_message)

    # reporting error
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
