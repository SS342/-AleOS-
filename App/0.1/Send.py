class SendMessage(object):
    def __init__(self, bot, _id):
        self.bot = bot
        self.id = _id

    def send_message(self, message: str):
        self.bot.send_message(self.id, message)