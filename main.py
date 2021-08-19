# let's write this code in 2 versions: 1. Eng 2. Per

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import functions, logging


def main(update, context):
    message = update.message.text.lower()

    if "ethereum" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.ethereum())
    elif "bitcoin" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.bitcoin())
    elif "coin" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.coin())
    elif "dollar" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.dollar())
    elif "euro" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.euro())
    elif "gold" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.gold())
    elif "pound" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.pound())
    elif "lire" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=functions.lire())
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="no currency with this name found")


# commands
start_handler = CommandHandler(['start', 'Start'], functions.start)
help_handler = CommandHandler(['Help', 'help'], functions.help)

# messages
main_handler = MessageHandler(Filters.text & ~Filters.command, main)
unsupported_message = MessageHandler((~Filters.text) & (~Filters.command), functions.help)


if __name__ == "__main__":

    # getting token from file
    token_file = open("token.txt", "r")
    tok = token_file.read()
    updater = Updater(token=tok, use_context=True)
    updater.start_polling()
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(main_handler)
    
    # reporting error
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

