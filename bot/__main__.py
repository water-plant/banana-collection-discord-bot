import os

import hikari
import crescent
import dotenv
from model import Model

dotenv.load_dotenv()

def on_ready():
    print("ready")
    return

if __name__ == "__main__":

    bot = hikari.RESTBot(
        token= os.environ["TOKEN"],
        token_type= "Bot",
        public_key=os.environ["PUBLIC_KEY"],
    )
    app = Model()
    client = crescent.Client(bot, app)
    bot.add_startup_callback(on_ready)

    bot.run()