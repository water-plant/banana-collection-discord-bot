import os

import hikari
import crescent
import dotenv
import model

dotenv.load_dotenv()



def main() -> int:

    bot = hikari.GatewayBot(
        token= os.environ["TOKEN"],
    )
    client = crescent.Client(bot, model.Model({}))
    client.plugins.load("mods.bananas")

    bot.run()


    return 0

if __name__ == "__main__":
    main()