import telegram, time


# getting token from file
token_file = open("token.txt", "r")
tok = token_file.read()

bot = telegram.Bot(token=tok)

# info of bot
print(bot.get_me())

# message hanlding

@bot.message_handler(commands=['start', 'Start', 'hello', 'Hello'])
def send_welcome(message):
    bot.reply_to(message, "خوش آمدید، ارز مورد نظر خود را تایپ کنید")

help_text = "برای مطلع شدن از قیمت ارز مورد نظر آن را تایپ کنید"
list_of_coins = "\n* دلار \n*یورو  \n* پوند \n* لیر\n* سکه\n* طلا\n* بیت کوین\n* اتر\n"
@bot.message_handler(commands=["help", 'Help'])
def send_help(message):
    bot.reply_to(message, help_text+list_of_coins)

@bot.message_handler(commands=["طلا"])
def tala(message):
    # finds the price and saves it in price variable
    price = None
    bot.reply_to(message," تومن"+ str(price)+" قیمت طلا : ")

@bot.message_handler(commands=["اتر"])
def eth(message):
    # finds the price and saves it in price variable
    price = None
    bot.reply_to(message," دلار"+ str(price)+" قیمت اتر : ")

@bot.message_handler(commands=["بیت کوین"])
def bitcoin(message):
    # finds the price and saves it in price variable
    price = None
    bot.reply_to(message," دلار"+ str(price)+" قیمت بیت کوین : ")

@bot.message_handler(commands=["سکه"])
def seke(message):
    # finds the price and saves it in price variable
    price = None
    bot.reply_to(message," تومن"+ str(price)+" قیمت سکه : ")

@bot.message_handler(commands=["لیر"])
def seke(message):
    # finds the price and saves it in price variable
    price = None
    bot.reply_to(message," تومن"+ str(price)+" قیمت لیر : ")

@bot.message_handler(commands=["پوند"])
def seke(message):
    # finds the price and saves it in price variable
    price = None
    bot.reply_to(message," تومن"+ str(price)+" قیمت پوند : ")

@bot.message_handler(commands=["یورو"])
def seke(message):
    # finds the price and saves it in price variable
    price = None
    bot.reply_to(message," تومن"+ str(price)+" قیمت یورو : ")

@bot.message_handler(commands=["دلار"])
def seke(message):
    # finds the price and saves it in price variable
    price = None
    bot.reply_to(message," تومن"+ str(price)+" قیمت دلار : ")

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(10)


