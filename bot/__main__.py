import os

import hikari
import crescent
import dotenv
import model

dotenv.load_dotenv()
class Main:
    def __init__(self, bot: hikari.GatewayBot):

        self.bot = bot
        self.client: crescent.Client = crescent.Client(bot, model.Model({}, {}))

        hikari.GatewayBot(
            token= os.environ["TOKEN"],
        )
        client = crescent.Client(bot, model.Model({}, {}))
        client.plugins.load("mods.bananas")


    def main(self) -> int:

        self.bot.run()

        return 0

if __name__ == "__main__":
    bot = hikari.GatewayBot(
            token= os.environ["TOKEN"],
        )
    Main(bot).main()