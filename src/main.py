from KahootBot import Bot

# Don't need to specify name as a random one will be generated, just specify a game pin
# Check README for details



bot = Bot(game_pin = "", name = "") 

########## Use ##########

with bot as k: 
  k.start()

########## OR ##########

bot.start()

#delete the one you're not using
