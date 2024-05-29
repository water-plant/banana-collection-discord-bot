import dataclasses
@dataclasses.dataclass
class Model:
    guild_id: int
    users: dict[int,int]

    def on_ready(self):
        print("ready")
        return