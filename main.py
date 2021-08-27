from KahootBot import Bot

# Don't need to specify name as a random one will be generated, just specify a game pin
# Check README for details


kahoot_bot = Bot(game_pin = "", name = "")
kahoot_bot.start()

########## OR ##########

Bot(game_pin = "", name = "").start()

########## OR ##########

with Bot(game_pin = "", name = "") as k: 
  k.start()

########## OR ##########

bot = Bot(game_pin = "", name = "") 

with bot as k: 
  k.start()
