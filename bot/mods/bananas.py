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
async def claim(ctx: crescent.Context) -> None:
    amount += data[ctx.user.id]
    data[ctx.user.id] = amount
    await ctx.respond(f"You now have {amount}")
    return

@plugin.include
@crescent.command
async def claim(ctx: crescent.Context) -> None:
    amount += data[ctx.user.id]
    data[ctx.user.id] = amount
    await ctx.respond(f"You now have {amount}")
    return