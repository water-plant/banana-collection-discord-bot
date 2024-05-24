import hikari
import crescent
import asyncio


with open("..\TOKEN", 'r') as file:
    token_str = file.readlines()

with open("..\SECRETS", 'r') as file:
    public_str = file.readlines()

bot = hikari.RESTBot(
    token= token_str,
    token_type= "Bot",
    public_key=public_str,
)
client = crescent.Client(bot)


bot.run()