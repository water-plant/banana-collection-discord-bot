import crescent
import crescent.context
import hikari
import typing


if typing.TYPE_CHECKING:
    from bot import Model

class Banana:

    plugin = crescent.Plugin[hikari.RESTBot, "Model"]()

    def __init__(self, client, guild_id:int, ):
        self.guild_id = guild_id
        return
    
    @plugin.include
    @crescent.command
    async def plugin_test(ctx: crescent.Context) -> None:
 