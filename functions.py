
# let's write this code in 2 versions: 1. Eng 2. Per

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#--------------------- FUNCTIONS -----------------------------------
def start(update, context):
    context.bot.send_mseeage(chat_id=update.effective_chat.id, text='send the name of a currency to get its price')

def ethereum():
    """ this command gets the price of ethereum from API and returns it """
    return "api call not implemented yet"

def bitcoin():
    """ this command gets the price of bitcoin from API and returns it """
    return "api call not implemented yet"

def gold():
    """ this command gets the price of gold from API and returns it """
    return "api call not implemented yet"

def coin():
    """ this command gets the price of coin from API and returns it """
    return "api call not implemented yet"

def dollar():
    """ this command gets the price of dollar from API and returns it """
    return "api call not implemented yet"

def pound():
    """ this command gets the price of pound from API and returns it """
    return "api call not implemented yet"

def euro():
    """ this command gets the price of euro from API and returns it """
    return "api call not implemented yet"

def lire():
    """ this command gets the price of lire from API and returns it """
    return "api call not implemented yet"
#------------------------------------------------------------------------------------

