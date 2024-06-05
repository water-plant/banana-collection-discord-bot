import crescent
import crescent.context
import hikari
import typing
#TODO: MAKE Database

if typing.TYPE_CHECKING:
    from bot import Model


plugin = crescent.Plugin[hikari.RESTBot, "Model"]()


@plugin.include
@crescent.command
async def plugin_test(ctx: crescent.Context) -> None:
    await ctx.respond("plugin functions")
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
                                   .add_field("`/claim` for daily claims\nyou will be able to passively gain bananas for a message sent every 5 minutes."))
    return

@plugin.include
@crescent.command
async def claim(ctx: crescent.Context) -> None:
    amount += data[ctx.user.id]
    data[ctx.user.id] = amount #some arbitrary database called data, will be changed later.
    await ctx.respond(f"You now have {amount}")
    return