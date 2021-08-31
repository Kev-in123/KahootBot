import time
import string
import random
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

web = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
web.get("https://kahoot.it")

buttons=['//*[@id="root"]/div/main/div[2]/div/div/button[1]',
         '//*[@id="root"]/div/main/div[2]/div/div/button[2]',
         '//*[@id="root"]/div/main/div[2]/div/div/button[3]',
         '//*[@id="root"]/div/main/div[2]/div/div/button[4]']

class Bot:
    def __init__(self, game_pin, name = None):
        self.game_pin = game_pin
        self.name = name or "".join(
            random.choice(f"{string.ascii_uppercase}{string.ascii_lowercase}{string.digits}")
            for n in range(7)
        )

    def __enter__(self):
        return self
        
    def __exit__(self, *args):
        pass

    def start(self):
 
        while True:
            try:
                id_textbox = web.find_element_by_xpath('//*[@id="game-input"]') 
                break
            except selenium.common.exceptions.NoSuchElementException:
                time.sleep(0.1)
        
        id_textbox.send_keys(self.game_pin)
        id_textbox.send_keys(Keys.ENTER)


        while True:
            try:
                name_textbox = web.find_element_by_xpath('//*[@id="nickname"]') 
                break
            except selenium.common.exceptions.NoSuchElementException:
                time.sleep(0.1)

        name_textbox.send_keys(self.name)
        name_textbox.send_keys(Keys.ENTER)

        while True:
            try:
                to_click = random.choice(buttons)
                button_box = web.find_element_by_xpath(to_click)
                button_box.click()
            except selenium.common.exceptions.NoSuchElementException:
                time.sleep(0.1)

    
