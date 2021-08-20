import requests
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler, PicklePersistence


def start(update, context):
    persian_output = "خوش اومدی به قیمت ارز، قیمت چه ارزی رو میخوای بدونی؟\n \
                      لیست ارز ها: /help"
    english_output = "welcome to Qeymate_Arz, what currency do you wnat to know the price of?\
                      \nlist of currencies: /help"
    new_user_output = "choose your language:\n\
                       زبان خود را انتخاب کنید:"

    if context.user_data.get("lang", None) == "en":
        context.bot.send_message(chat_id=update.effective_chat.id, text=english_output)
    elif context.user_data.get("lang", None) == "pe":
        context.bot.send_message(chat_id=update.effective_chat.id, text=persian_output)
    else:
        # new user
        ikeyboard = [[InlineKeyboardButton(text="English", callback_data="lang_en"),
                      InlineKeyboardButton(text="Persian", callback_data="lang_pe")]]
        imarkup = InlineKeyboardMarkup(ikeyboard)
        context.bot.send_message(chat_id=update.effective_chat.id, text=new_user_output, reply_markup=imarkup)

def lang(update, context):
    """ this function will be called when the users chooses a language with inline keyboard
        it will make a set the "lang" key in user_data dictionary
        user_data is a dictionary provided by python-telegram-bot
        more info https://github.com/python-telegram-bot/python-telegram-bot/wiki/Storing-bot%2C-user-and-chat-related-data"""

    query = update.callback_query
    query.answer()  # according to telegram api, all queries must be answered

    if query.data == "lang_en":
        query.edit_message_text(text="language set to English")
        context.user_data["lang"]="en"
    elif query.data == "lang_pe":
        query.edit_message_text(text="زبان فارسی انتخاب شد")
        context.user_data["lang"]="pe"
    
    start(update, context)  # this way the user sees the start message after choosing language

def help(update, context):
    if not context.user_data.get("lang", None):
        # new user
        start(update, context)
    elif context.user_data.get("lang", None) == "en":
        # send english help
        list_of_currencies = ['gold', 'dollar', 'etherium', 'bitcoin', 'coin', 'pound', 'euro', 'lire']
        vertical_list_currencies = ''
        for item in list_of_currencies:
            vertical_list_currencies += "** " + item.ljust(8) + "\n"
        context.bot.send_message(chat_id=update.effective_chat.id, text='print one of these currencies to get the price\n' + vertical_list_currencies )

    elif context.user_data.get("lang", None) == "pe":
        # send persian help
        list_of_currencies = ['طلا', 'دلار', 'اتر', 'بیت کوین', 'سکه', 'پوند', 'یورو', 'لیر']
        vertical_list_currencies = ''
        for item in list_of_currencies:
            vertical_list_currencies += "** " + item.ljust(8) + "\n"
        context.bot.send_message(chat_id=update.effective_chat.id, text='اسم یکی از این ارزها رو بفرست تا قیمتش رو ببینی\n' + vertical_list_currencies)


def ethereum(lang):
    """ this command gets the price of ethereum from API and returns it """
    # get the price of etherium, until 2 decimal number, based on US dollar
    etherium_info = requests.get("https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT")
    ethusdt = format(float(etherium_info.json()["price"]), '.2f')

    if lang == "en":
        return "ethereum : $ " + ethusdt
    elif lang == "pe":
        return " دلار" + ethusdt +"اتریوم : "

def bitcoin(lang):
    """ this command gets the price of bitcoin from API and returns it """
    # get the bitcoin price, until 2 decimal number, based on US dollar
    bitcoin_info = requests.get("https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT")
    btcusdt = format(float(bitcoin_info.json()["price"]), '.2f')

    if lang == "en":
        return "bitcoin : $ " + btcusdt
    elif lang == "pe":
        return " دلار" + btcusdt + "بیت کوین : "


def gold(lang):
    """ this command gets the price of gold from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/geram18")

    if lang == "en":
        return "gold(per gram) : " + format(price/10000000, '.3f') + " mTomans"
    elif lang == "pe":
        return " هزارتومان" + format(price/10000000, '.3f') + "طلا : "

def coin(lang):
    """ this command gets the price of coin from API and returns it """
    price_1 = give_price_websites_1("https://www.tgju.org/profile/sekeb")
    price_2 = give_price_websites_1("https://www.tgju.org/profile/nim")
    price_3 = give_price_websites_1("https://www.tgju.org/profile/rob")
    output_1 = "*Coin*\n\n              coin : " + format(price_1/10000000, '.3f') + " mTomans\n"
    output_2 = "      coin-half :   " +format(price_2/10000000, '.3f') + " mTomans\n"
    output_3 = "coin-quarter :   " +format(price_3/10000000, '.3f') + " mTomans\n"
    return output_1 + output_2 + output_3

def dollar(lang):
    """ this command gets the price of dollar from API and returns it """
    price = give_price_website_2("https://www.tgju.org/%D9%82%DB%8C%D9%85%D8%AA-%D8%AF%D9%84%D8%A7%D8%B1")

    if lang == "en":
        return "dollar : " + format(price/10000, '.2f') + " kTomans"
    elif lang == "pe":
        return " هزارتومان" + format(price/10000000, '.3f') + "دلار : "

def pound(lang):
    """ this command gets the price of pound from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/price_gbp")

    if lang == "en":
        return "pound : " + format(price/10000, '.2f') + ' kTomans'
    elif lang == "pe":
        return " هزارتومان" + format(price/10000000, '.3f') + "پوند : "

def euro(lang):
    """ this command gets the price of euro from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/price_eur")

    if lang == "en":
        return "euro : " + format(price/10000, '.2f') + ' kTomans'
    elif lang == "pe":
        return " هزارتومان" + format(price/10000000, '.3f') + "یورو : "

def lire(lang):
    """ this command gets the price of lire from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/price_try")

    if lang == "en":
        return "lire : " + format(price / 10000, '.2f') + '0' + ' kTomans'
    elif lang == "pe":
        return " هزارتومان" + format(price/10000000, '.3f') + '0' + "لیر : "

#-------- 3 needed functions to read info from websites, for all except dollar

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

#-------------------------------------------------------------------------------------------
# for dollar, as they are 2 kinds if dollar, i had to read this from different source and format
def give_price_website_2(url):
    info = requests.get(url).text
    index = info.find("اعلام شده است")
    info = info[index-40:index]
    price = find_num(info)
    return price
