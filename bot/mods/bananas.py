import crescent
import crescent.context
import hikari
import typing
from crescent.ext import tasks

if typing.TYPE_CHECKING:
    from bot.model import Model

#TODO: MAKE Database


plugin = crescent.Plugin[hikari.GatewayBot, "Model"]()

@plugin.include
@crescent.event
async def on_ready(e: hikari.events.lifetime_events.StartingEvent):
    if(e):
        print("ready")
    return

@plugin.include
@crescent.command
async def plugin_test(ctx: crescent.Context) -> None:
    await ctx.respond("plugin functions", ephemeral=True)
    return

 
@plugin.include
@crescent.command
async def instructions(ctx: crescent.Context) -> None:
    """
    This may be changed as I turn this into a web application. This could also be a separate from the web game. 
    bananas are just a measure of server activity.
    \nThere will be a dashboard to display them
    """

    await ctx.respond(embed=
                      hikari.Embed(title="instructions",
                                   description="instructions to using this bot")
                                   .set_footer("github link here")
                                   .add_field(name= "body", value="`/claim` for daily claims\nyou will be able to passively gain bananas for a message sent every 5 minutes."),
                    ephemeral=True)
    return

@plugin.include
@crescent.command
async def claim(ctx: crescent.Context) -> None:
    amount = plugin.model.calculate_bananas(ctx.user.id, ctx.guild.id)
    await ctx.respond(f"You now have {amount} bananas")
    return


@plugin.include
@crescent.command(name="profile")
class Profile():
    mention = crescent.option(hikari.User, default=None)


    def valid_Option(self, uid) -> hikari.snowflakes.Snowflake:
        return self.mention.id if self.mention else uid

    async def callback(self, ctx: crescent.Context):
        embed_created: hikari.Embed = hikari.Embed(title="Profile", description=f"You have {plugin.model.users[self.valid_Option(ctx.user.id)]}").set_footer("github link here")
        await ctx.respond(embed = embed_created)        
        return


@plugin.include
@crescent.event
async def on_message(e: hikari.MessageCreateEvent) -> None:
    if(e.message.author.is_bot):
        return
    plugin.model.add_to_set(e.message.author.id,e.message.guild_id)
    return
    

@plugin.include
@tasks.loop(seconds=30)
async def loop():
    for guild_key in plugin.model.guild_users_chatted_map.keys():
        for user_key in plugin.model.guild_users_chatted_map[guild_key]:
            
            plugin.model.users[user_key][guild_key] += 5
    print("looped")