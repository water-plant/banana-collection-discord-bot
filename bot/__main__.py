import os

import hikari
import crescent
import dotenv
from model import Model

dotenv.load_dotenv()

def on_ready():
    print("ready")
    return

def main() -> int:

    bot = hikari.RESTBot(
        token= os.environ["TOKEN"],
        token_type= "Bot",
        public_key=os.environ["PUBLIC_KEY"],
    )
    app = Model()
    client = crescent.Client(bot, app)
    bot.add_startup_callback(on_ready)

    bot.run()


    return 0 

if __name__ == "__main__":
    main()