import requests
from main import users_language

def start(update, context):
    output_persian = "خوش اومدی به قیمت ارز، قیمت چه ارزی رو میخوای بدونی؟"
    output_english = "\nwelcome to Qeymate_Arz, what currency do you wnat to know the price of?"

    # decide the language
    if update.effective_chat.id not in users_language.keys():
        # new user
        context.bot.send_message(chat_id=update.effective_chat.id, text="choose your language (P: presian / E: english) ")
    else:
        # not a new user
        if users_language[update.effective_chat.id] == "persian":
            # persian
            output = output_persian
        else:
            # english
            output = output_english

    context.bot.send_message(chat_id=update.effective_chat.id, text=output)

def help(update, context):

    if main.users_language[update.effective_chat.id] == "english":
        # send english help
        list_of_currencies = ['gold', 'dollar', 'etherium', 'bitcoin', 'coin', 'pound', 'euro', 'lire']
        vertical_list_currencies = ''
        for item in list_of_currencies:
            vertical_list_currencies += "** " + item.ljust(8) + "\n"
        context.bot.send_message(chat_id=update.effective_chat.id, text='print one of these currencies to get the price\n' + vertical_list_currencies )

    elif main.users_language[update.effective_chat.id] == "persian":
        # send persian help
        list_of_currencies = ['طلا', 'دلار', 'اتر', 'بیت کوین', 'سکه', 'پوند', 'یورو', 'لیر']
        vertical_list_currencies = ''
        for item in list_of_currencies:
            vertical_list_currencies += "** " + item.ljust(8) + "\n"
        context.bot.send_message(chat_id=update.effective_chat.id, text='print one of these currencies to get the price\n' + vertical_list_currencies)


def ethereum():
    """ this command gets the price of ethereum from API and returns it """
    # get the price of etherium, until 2 decimal number, based on US dollar
    etherium_info = requests.get("https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT")
    ethusdt = format(float(etherium_info.json()["price"]), '.2f')

    if main.users_language[update.effective_chat.id] == "english":
        return "etherium : $ " + ethusdt
    elif main.users_language[update.effective_chat.id] == "persian":
        return " دلار" + ethusdt +"اتریوم : "

def bitcoin():
    """ this command gets the price of bitcoin from API and returns it """
    # get the bitcoin price, until 2 decimal number, based on US dollar
    bitcoin_info = requests.get("https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT")
    btcusdt = format(float(bitcoin_info.json()["price"]), '.2f')

    if main.users_language[update.effective_chat.id] == "english":
        return "bitcoin : $ " + btcusdt
    elif main.users_language[update.effective_chat.id] == "persian":
        return " دلار" + btcusdt + "بیت کوین : "


def gold():
    """ this command gets the price of gold from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/geram18")

    if main.users_language[update.effective_chat.id] == "english":
        return "gold(per gram) : " + format(price/10000000, '.3f') + " mTomans"
    elif main.users_language[update.effective_chat.id] == "persian":
        return " هزارتومان" + format(price/10000000, '.3f') + "طلا : "

def coin():
    """ this command gets the price of coin from API and returns it """
    price_1 = give_price_websites_1("https://www.tgju.org/profile/sekeb")
    price_2 = give_price_websites_1("https://www.tgju.org/profile/nim")
    price_3 = give_price_websites_1("https://www.tgju.org/profile/rob")
    output_1 = "*Coin*\n\n              coin : " + format(price_1/10000000, '.3f') + " mTomans\n"
    output_2 = "      coin-half :   " +format(price_2/10000000, '.3f') + " mTomans\n"
    output_3 = "coin-quarter :   " +format(price_3/10000000, '.3f') + " mTomans\n"
    return output_1 + output_2 + output_3

def dollar():
    """ this command gets the price of dollar from API and returns it """
    price = give_price_website_2("https://www.tgju.org/%D9%82%DB%8C%D9%85%D8%AA-%D8%AF%D9%84%D8%A7%D8%B1")

    if main.users_language[update.effective_chat.id] == "english":
        return "dollar : " + format(price/10000, '.2f') + " kTomans"
    elif main.users_language[update.effective_chat.id] == "persian":
        return " هزارتومان" + format(price/10000000, '.3f') + "دلار : "

def pound():
    """ this command gets the price of pound from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/price_gbp")

    if main.users_language[update.effective_chat.id] == "english":
        return "pound : " + format(price/10000, '.2f') + ' kTomans'
    elif main.users_language[update.effective_chat.id] == "persian":
        return " هزارتومان" + format(price/10000000, '.3f') + "پوند : "

def euro():
    """ this command gets the price of euro from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/price_eur")

    if main.users_language[update.effective_chat.id] == "english":
        return "euro : " + format(price/10000, '.2f') + ' kTomans'
    elif main.users_language[update.effective_chat.id] == "persian":
        return " هزارتومان" + format(price/10000000, '.3f') + "یورو : "

def lire():
    """ this command gets the price of lire from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/price_try")

    if main.users_language[update.effective_chat.id] == "english":
        return "lire : " + format(price / 10000, '.2f') + '0' + ' kTomans'
    elif main.users_language[update.effective_chat.id] == "persian":
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
