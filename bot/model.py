import dataclasses
import random, hikari

@dataclasses.dataclass
class Model:
    users: dict[hikari.snowflakes.Snowflake,int] | None


    def is_valid_key(self, uid:hikari.snowflakes.Snowflake):
        if not self.users.get(uid):
            self.users[uid] = 0
        return

    def calculate_bananas(self, uid:hikari.snowflakes.Snowflake) -> int:
        self.is_valid_key(uid)
        val = self.users[uid]
        self.users[uid] = val + int(random.randint(1,10))
        return self.users[uid]
    