import requests, logging, emoji
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler, PicklePersistence, CommandHandler, MessageHandler, Filters, Updater


def start(update, context):
    name_gretting = update.effective_user.first_name + emoji.emojize(":waving_hand:\n\n")
    persian_output = "خوش اومدی به قیمت ارز، قیمت چه ارزی رو میخوای بدونی؟\n\n\n \
                      لیست ارز ها: /help"
    english_output = "welcome to Qeymate_Arz, what currency do you wnat to know the price of?\
                      \n\n\nlist of currencies: /help"
    new_user_output = "choose your language:\n\
                       زبان خود را انتخاب کنید:"

    if context.user_data.get("lang", None) == "en":
        context.bot.send_message(chat_id=update.effective_chat.id, text=name_gretting + english_output)
    elif context.user_data.get("lang", None) == "pe":
        context.bot.send_message(chat_id=update.effective_chat.id, text=name_gretting + persian_output)
    else:
        # new user
        # creataing list of two buttons with specefic call back info
        ikeyboard_button = [[InlineKeyboardButton(text="English", callback_data="en"),
                      InlineKeyboardButton(text="Persian", callback_data="pe")]]
        imarkup = InlineKeyboardMarkup(ikeyboard_button)
        context.bot.send_message(chat_id=update.effective_chat.id, text=new_user_output, reply_markup=imarkup)


def lang(update, context):
    """ this function will be called when the users chooses a language with inline keyboard
        it will make a set the "lang" key in user_data dictionary
        user_data is a dictionary provided by python-telegram-bot
        more info https://github.com/python-telegram-bot/python-telegram-bot/wiki/Storing-bot%2C-user-and-chat-related-data"""

    query = update.callback_query
    query.answer()  # according to telegram api, all queries must be answered

    if query.data == "en":
        query.edit_message_text(text="language set to English")
        context.user_data["lang"] = "en"
    elif query.data == "pe":
        query.edit_message_text(text="زبان فارسی انتخاب شد")
        context.user_data["lang"] = "pe"

    start(update, context)  # this way the user sees the start message after choosing language


def help(update, context):
    if not context.user_data.get("lang", None):
        # new user
        start(update, context)
    elif context.user_data.get("lang", None) == "en":
        # send english help
        list_of_currencies = ['gold', 'dollar', 'etherium', 'bitcoin', 'coin', 'pound', 'euro', 'lire']
        vertical_list_currencies = emoji.emojize(" :yellow_circle: gold\n") + emoji.emojize(" :United_States: dollar\n") + emoji.emojize(" :gem_stone: etherium\n") +emoji.emojize(" :money_bag: bitcoin\n") + emoji.emojize(" :Iran: coin\n") + emoji.emojize(" :United_Kingdom: pound\n") +emoji.emojize(" :European_Union: euro\n") + emoji.emojize(" :Turkey: lire\n")

        context.bot.send_message(chat_id=update.effective_chat.id, text='print one of these currencies to get the price : \n\n' + vertical_list_currencies)

    elif context.user_data.get("lang", None) == "pe":
        # send persian help
        list_of_currencies = ['طلا', 'دلار', 'اتر', 'بیت کوین', 'سکه', 'پوند', 'یورو', 'لیر']
        vertical_list_currencies = ""
        for item in list_of_currencies:
            vertical_list_currencies += "** " + item.ljust(8) + "\n"
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='اسم یکی از این ارزها رو بفرست تا قیمتش رو ببینی\n' + vertical_list_currencies)

def language_choose(update, context):
    # this function lets user to change the language whenever (s)he desired
    inline_keyboard_buttons = [[InlineKeyboardButton(text="English", callback_data="en")],
                               [InlineKeyboardButton(text="فارسی", callback_data="pe")]]
    # creating the keyboard using two buttons
    creating_inline_keyboard = InlineKeyboardMarkup(inline_keyboard_buttons)

    text_for_choosing_lan = "choose your language:\n\
                       زبان خود را انتخاب کنید:"

    context.bot.send_message(chat_id=update.effective_chat.id,text=text_for_choosing_lan , reply_markup=creating_inline_keyboard)

def ethereum(lang):
    """ this command gets the price of ethereum from API and returns it """
    # get the price of etherium, until 2 decimal number, based on US dollar
    etherium_info = requests.get("https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT")
    ethusdt = format(float(etherium_info.json()["price"]), '.2f')

    if lang == "en":
        return "ethereum : $ " + ethusdt
    elif lang == "pe":
        return  "اتریوم : " + " دلار " + ethusdt


def bitcoin(lang):
    """ this command gets the price of bitcoin from API and returns it """
    # get the bitcoin price, until 2 decimal number, based on US dollar
    bitcoin_info = requests.get("https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT")
    btcusdt = format(float(bitcoin_info.json()["price"]), '.2f')

    if lang == "en":
        return "bitcoin : $ " + btcusdt
    elif lang == "pe":
        return  "اتریوم : " + " دلار " + btcusdt


def gold(lang):
    """ this command gets the price of gold from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/geram18")

    if lang == "en":
        return "gold(per gram) : " + format(price / 10000000, '.3f') + " mTomans"
    elif lang == "pe":
        return "طلا : " + " میلیون تومان " + format(price / 10000000, '.3f')


def coin(lang):
    """ this command gets the price of coin from API and returns it """
    price_1 = give_price_websites_1("https://www.tgju.org/profile/sekeb")
    price_2 = give_price_websites_1("https://www.tgju.org/profile/nim")
    price_3 = give_price_websites_1("https://www.tgju.org/profile/rob")

    if lang == "en":
        output_1 = "Coin\n\n              coin : " + format(price_1 / 10000000, '.3f') + " mTomans\n"
        output_2 = "      coin-half :   " + format(price_2 / 10000000, '.3f') + " mTomans\n"
        output_3 = "coin-quarter :   " + format(price_3 / 10000000, '.3f') + " mTomans\n"
        return output_1 + output_2 + output_3
    elif lang == "pe":
        out_put_0 = "**سکه**\n"
        output_1 = "سکه تمام بهار آزادی : " + format(price_1 / 10000000, '.3f') + " میلیون تومان \n"
        output_2 = "نیم سکه : " + format(price_2 / 10000000, '.3f') + " میلیون تومان \n"
        output_3 = "ربع سکه : " + format(price_3 / 10000000, '.3f') + " میلیون تومان \n"
    return out_put_0 + output_1 + output_2 + output_3


def dollar(lang):
    """ this command gets the price of dollar from API and returns it """
    price = give_price_website_2("https://www.tgju.org/%D9%82%DB%8C%D9%85%D8%AA-%D8%AF%D9%84%D8%A7%D8%B1")

    if lang == "en":
        return "dollar : " + format(price / 10000, '.2f') + " kTomans"
    elif lang == "pe":
        return "دلار : " + " هزارتومان " + format(price / 10000, '.3f')


def pound(lang):
    """ this command gets the price of pound from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/price_gbp")

    if lang == "en":
        return "pound : " + format(price / 10000, '.2f') + ' kTomans'
    elif lang == "pe":
        return "پوند : " + " هزارتومان " + format(price / 10000, '.3f')


def euro(lang):
    """ this command gets the price of euro from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/price_eur")

    if lang == "en":
        return "euro : " + format(price / 10000, '.2f') + ' kTomans'
    elif lang == "pe":
        return "یورو : " + " هزارتومان " + format(price / 10000, '.3f')


def lire(lang):
    """ this command gets the price of lire from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/price_try")

    if lang == "en":
        return "lire : " + format(price / 10000, '.2f') + '0' + ' kTomans'
    elif lang == "pe":
        return "لیر : " + " هزارتومان " + format(price / 10000, '.3f')


# -------- 3 needed functions to read info from websites, for all except dollar

# finds 2nd occurance of نرخ فعلی, this is because of the structure  of that website
# first نرخ فعلی does not have price near that
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)


# when we found a string that contains price in it (other characters as well),
#  this will find the price and returns  it
def find_num(string):
    number = ''
    for char in string:
        if char.isnumeric():
            number += char
    return float(number)


# gives a URL and finds the price
def give_price_websites_1(url):
    info = requests.get(url).text
    index = find_2nd(info, "نرخ فعلی")
    info = info[index:index + 95]
    price = find_num(info)
    return price


# -------------------------------------------------------------------------------------------
# for dollar, as they are 2 kinds if dollar, i had to read this from different source and format
def give_price_website_2(url):
    info = requests.get(url).text
    index = info.find("اعلام شده است")
    info = info[index - 40:index]
    price = find_num(info)
    return price


# -------------------------------- hanlding all maessages by user --------------------------------
def main(update, context):

    message = update.message.text.lower()
    if "ethereum" in message or "اتر" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=emoji.emojize(" :gem_stone: \n")+ethereum(context.user_data.get("lang", None)))
    elif "bitcoin" in message or "بیتکوین" in message or "بیت کوین" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=emoji.emojize(" :money_bag: \n")+bitcoin(context.user_data.get("lang", None)))
    elif "coin" in message or "سکه" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=emoji.emojize(" :coin: \n")+coin(context.user_data.get("lang", None)))
    elif "dollar" in message or "دلار" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=emoji.emojize(" :United_States: \n")+dollar(context.user_data.get("lang", None)))
    elif "euro" in message or "یورو" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=emoji.emojize(" :European_Union: \n")+euro(context.user_data.get("lang", None)))
    elif "gold" in message or "طلا" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=emoji.emojize(" :yellow_circle: \n")+gold(context.user_data.get("lang", None)))
    elif "pound" in message or "پوند" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=emoji.emojize(" :United_Kingdom: \n")+pound(context.user_data.get("lang", None)))
    elif "lire" in message or "لیر" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text=emoji.emojize(" :Turkey: \n")+lire(context.user_data.get("lang", None)))
    else:
        if context.user_data.get("lang", None) == "pe":
            context.bot.send_message(chat_id=update.effective_chat.id, text="ارزی به این نام یافت نشد")
        else :
            context.bot.send_message(chat_id=update.effective_chat.id, text="no currency with this name found")

# ------------------------- working with telegram API -------------------------------------------

# commands
start_handler = CommandHandler(['start', 'Start'], start)
help_handler = CommandHandler(['Help', 'help'], help)


# messages
main_handler = MessageHandler(Filters.text & ~Filters.command, main)
unsupported_message = MessageHandler((~Filters.text) & (~Filters.command), help)

# query
language = CallbackQueryHandler(lang)

# command for changing language
language_choose_handler = CommandHandler(["language", "Language"], language_choose)

if __name__ == "__main__":
    # getting token from file
    with open("token.txt", "rt") as token_file:
        tok = token_file.read()

    updater = Updater(token=tok, use_context=True)

    updater.start_polling()

    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(language_choose_handler)
    dispatcher.add_handler(main_handler)
    dispatcher.add_handler(unsupported_message)
    dispatcher.add_handler(language)


    # reporting error
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)