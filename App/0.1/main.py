from vkCheker import VkChecker
from config import Config
import telebot
from Send import SendMessage
import vk

config = Config()

Sender = SendMessage(telebot.TeleBot(config.token), config.main_user_id)
Sender.send_message("Привет")
vkc = VkChecker(vk.API(access_token=config.vk_token))

def run():
    while True:
        vkc.check_update()