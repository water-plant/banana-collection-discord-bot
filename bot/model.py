import dataclasses
import random, hikari

@dataclasses.dataclass
class Model:
    guild_id: int
    users: dict[str,int]

    def calculate_bananas(self, uid:str) -> None:
        val = self.users[uid]
        self.users[uid] = val + int(random.randint(1,10))
        return