from KahootBot import Bot

#dont need to specify name as a random one will be generated

kahoot_bot = Bot(game_pin="", name="")
kahoot_bot.start()

########## OR ##########

with Bot(game_pin="", name="") as k:
  k.start()
