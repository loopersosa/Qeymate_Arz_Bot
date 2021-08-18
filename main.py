import telegram, time


# getting token from file
token_file = open("token.txt", "r")
tok = token_file.read()

bot = telegram.Bot(token=tok)

# info of bot
print(bot.get_me())
