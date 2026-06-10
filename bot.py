import os
import sys

# Set working directory to the project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)
sys.path.insert(0, BASE_DIR)

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

SESSION_PATH = os.path.join(BASE_DIR, "aryan_login")

class Bot(Client):

    def __init__(self):
        super().__init__(
            SESSION_PATH,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="TechVJ", path=BASE_DIR),
            workers=50,
            sleep_threshold=10
        )

    async def start(self):
        await super().start()
        print('Bot Started Powered By @VJ_Botz')

    async def stop(self, *args):
        await super().stop()
        print('Bot Stopped Bye')

Bot().run()
