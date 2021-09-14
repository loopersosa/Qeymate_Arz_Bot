from os import times
import telebot, emoji, requests, jdatetime
from telebot import types
from keep import keep_alive

# importing token
with open("token.txt", "r") as p:
    TOKEN = p.read()
    #print(TOKEN)

# initializing bot    
bot = telebot.TeleBot(TOKEN)



def main(message):
    
    #print(message)
    chat_ID = message.chat.id
    message = message.text.lower()
    # time = datetime.datetime.now().strftime("\n%X") + emoji.emojize(" :watch: ") + datetime.datetime.now().strftime("\n%x") + emoji.emojize(" :calendar: ") 
    # saat = datetime.datetime.now().strftime("%X")
    jdatetime.set_locale('fa_IR')
    time =jdatetime.datetime.now().strftime("%c")
    if "eth" in message or "اتر" in message:
        bot.send_message( chat_id=chat_ID , text=emoji.emojize(" :gem_stone: ")+ ethereum() +"\n"+time)
    elif "bitcoin" in message or "بیتکوین" in message or "بیت کوین" in message:
        bot.send_message(chat_id=chat_ID, text=emoji.emojize(" :money_bag: ")+bitcoin()+"\n"+time)
    elif "coin" in message or "سکه" in message:
        bot.send_message(chat_id=chat_ID, text=emoji.emojize(" :coin: ")+coin()+"\n"+time)
    elif "dollar" in message or "دلار" in message:
        bot.send_message(chat_id=chat_ID, text=emoji.emojize(" :United_States: ")+dollar()+"\n"+time)
    elif "euro" in message or "یورو" in message:
        bot.send_message(chat_id=chat_ID, text=emoji.emojize(" :European_Union: ")+euro()+"\n"+time)
    elif "gold" in message or "طلا" in message:    
        bot.send_message(chat_id=chat_ID, text=emoji.emojize(" :yellow_circle: ")+gold()+"\n"+time)
    elif "pound" in message or "پوند" in message:
        bot.send_message(chat_id=chat_ID, text=emoji.emojize(" :United_Kingdom: ")+pound()+"\n"+time)
    elif "lire" in message or "لیر" in message:
        bot.send_message(chat_id=chat_ID, text=emoji.emojize(" :Turkey: ")+lire()+"\n"+time)
    elif "کون" in message or "کیر" in message or "کص" in message :
        bot.send_message(chat_id=chat_ID, text="حیف که اسلام دست و بالم رو بسته \nوگرنه نشونت میدادم")
    else:
        bot.send_message(chat_id=chat_ID, text="پیدا نکردم هیچی")

def ethereum():
    """ this command gets the price of ethereum from API and returns it """
    # get the price of etherium, until 2 decimal number, based on US dollar
    etherium_info = requests.get("https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT")
    ethusdt = format(float(etherium_info.json()["price"]), '.2f')
    return "اتریوم : $ " + ethusdt

def bitcoin():
    """ this command gets the price of bitcoin from API and returns it """
    # get the bitcoin price, until 2 decimal number, based on US dollar
    bitcoin_info = requests.get("https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT")
    btcusdt = format(float(bitcoin_info.json()["price"]), '.2f')


    return "بیتکوین : $ " + btcusdt


def gold():
    """ this command gets the price of gold from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/geram18")
    return "طلا(گرمی) : " + format(price / 10000000, '.3f') + " میلیون تومان"

def coin():
    """ this command gets the price of coin from API and returns it """
    price_1 = give_price_websites_1("https://www.tgju.org/profile/sekeb")
    price_2 = give_price_websites_1("https://www.tgju.org/profile/nim")
    price_3 = give_price_websites_1("https://www.tgju.org/profile/rob")
    output_1 = "سکه\n\n  سکه تمام بهار آزادی : " + format(price_1 / 10000000, '.3f') + " میلیون تومان\n"       
    output_2 = "                 نیم سکه :  " + format(price_2 / 10000000, '.3f')+ " " + " میلیون تومان\n"
    output_3 = "                 ربع سکه :  " + format(price_3 / 10000000, '.3f') + " " + " میلیون تومان\n"
    return output_1 + output_2 + output_3



def dollar():
    """ this command gets the price of dollar from API and returns it """
    price = give_price_website_2("https://www.tgju.org/%D9%82%DB%8C%D9%85%D8%AA-%D8%AF%D9%84%D8%A7%D8%B1")
    return "دلار : " + format(price / 10000, '.2f') + " هزارتومان"



def pound():
    """ this command gets the price of pound from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/price_gbp")
    return "پوند : " + format(price / 10000, '.2f') + ' هزارتومان'



def euro():
    """ this command gets the price of euro from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/price_eur")
    return "یورو : " + format(price / 10000, '.2f') + 'هزارتومان  '



def lire():
    """ this command gets the price of lire from API and returns it """
    price = give_price_websites_1("https://www.tgju.org/profile/price_try")
    return "لیر : " + format(price / 10000, '.2f') + '0' + ' هزارتومان'



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

@bot.message_handler(commands=['start', 'Start'])
def start(message):
  name = message.from_user.first_name

  # to know who visited the bot
  jdatetime.set_locale('fa_IR')
  
  with open("names.txt", "a") as people:
    
    first_name = message.from_user.first_name
    user_id = message.from_user.username

    if user_id != None:
      info_line = first_name + " " + user_id + " " + jdatetime.datetime.now().strftime("%c") + "\n"
      people.writelines(info_line)
    else:
      info_line = first_name + " " + jdatetime.datetime.now().strftime("%c") + "\n"
      people.writelines(info_line)
    print(info_line)

  TEXT = " سلام " + name + emoji.emojize(" :waving_hand:") + "\n\nبرای کمک آماده‌ام" + "\n /help "
  bot.send_message(chat_id=message.chat.id, text=TEXT )

@bot.message_handler(commands=['help', 'Help'])
def help(message):
    vertical_list_currencies = emoji.emojize(" :yellow_circle: طلا\n") + emoji.emojize(" :United_States: دلار\n") + emoji.emojize(" :gem_stone: اتریوم\n") +emoji.emojize(" :money_bag: بیتکوین\n") + emoji.emojize(" :Iran: سکه\n") + emoji.emojize(" :United_Kingdom: پوند\n") +emoji.emojize(" :European_Union: یورو\n") + emoji.emojize(" :Turkey: لیر\n")
    markup = types.ReplyKeyboardMarkup()
    dollar = types.KeyboardButton(emoji.emojize(" :United_States: دلار\n"))
    pound = types.KeyboardButton(emoji.emojize(" :United_Kingdom: پوند\n"))
    lire = types.KeyboardButton(emoji.emojize(" :Turkey: لیر\n"))
    coin = types.KeyboardButton(emoji.emojize(" :Iran: سکه\n"))
    gold = types.KeyboardButton(emoji.emojize(" :yellow_circle: طلا\n"))
    bitcoin = types.KeyboardButton(emoji.emojize(" :money_bag: بیتکوین\n"))
    eth = types.KeyboardButton(emoji.emojize(" :gem_stone: اتریوم\n"))
    euro = types.KeyboardButton(emoji.emojize(" :European_Union: یورو\n"))
    markup.row(dollar, euro)
    markup.row(coin, gold)
    markup.row(bitcoin, pound, lire, eth)
    bot.send_message(message.chat.id, text='ارز مورد نظر را انتخاب کنید : \n\n' + vertical_list_currencies, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main_handler(message):
	main(message)

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message):
	bot.reply_to(message, " جدا فکر کردی میتونی با استیکر فرستادن منو دست بنداری؟ ")

@bot.message_handler(content_types=['photo', 'audio', 'video', 'voice', "document", 'video_note', 'location'])
def PAV_handler(message):
	bot.reply_to(message, " خب الان من با این چی کنم ")

@bot.message_handler(content_types=['animation'])
def gif_handler(message):
    bot.reply_to(message, text="(@magatowski) گیف هاتو بفرست برای مهدی ")
'''while True:
  try:
    bot.stop_polling()
    bot.remove_webhook()
    keep_alive()
    bot.infinity_polling()
  except Exception as e:
    logging.info(e)
    bot.remove_webhook()  
    keep_alive()
    bot.stop_polling()
    bot.infinity_polling()'''

keep_alive()  
bot.infinity_polling()


