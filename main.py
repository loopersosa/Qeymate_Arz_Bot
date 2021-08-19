
# let's write this code in 2 versions: 1. Eng 2. Per

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import functions, logging

# getting token from file
token_file = open("token.txt", "r")
tok = token_file.read()

# commands
start_handler = CommandHandler(['start', 'Start'], functions.start)
help_handler = CommandHandler(['Help', 'help'], functions.help)

# main function
def main(update, context):
    message = update.message.text
    if "ethereum" in message.lower():
        context.bot.send_message(chat_id=update.effective_chat.id, text=ethereum())

    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="no currency with this name found")

# messages
main_handler = MessageHandler(Filters.text & ~Filters.command, main)

if __name__ == "__main__":
    updater = Updater(token=tok, use_context=True)
    updater.start_polling()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(main_handler)



