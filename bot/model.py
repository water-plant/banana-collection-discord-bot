import dataclasses
import random, hikari

@dataclasses.dataclass
class Model:
    #users: dict[hikari.snowflakes.Snowflake, int]
    users: dict[hikari.snowflakes.Snowflake, dict[hikari.snowflakes.Snowflake,int] ]
    guild_users_chatted_map: dict[hikari.snowflakes.Snowflake, set[hikari.snowflakes.Snowflake] ] | None


    #TODO: add new user method

    def is_valid_key(self, uid:hikari.snowflakes.Snowflake, guild:hikari.snowflakes.Snowflake):
        if not self.users.get(uid):
            self.users[uid]= {guild:0}
        elif not self.users.get(uid).get(guild):
            self.users[uid][guild] = 0

        return
    
    def get_bananas(self, uid:hikari.snowflakes.Snowflake, guild:hikari.snowflakes.Snowflake)-> int:
        return self.users[uid][guild]

    def set_bananas(self, uid:hikari.snowflakes.Snowflake, guild:hikari.snowflakes.Snowflake)-> int:
        self.users[uid][guild] += 5

    def calculate_bananas(self, uid:hikari.snowflakes.Snowflake, guild:hikari.snowflakes.Snowflake) -> int:
        self.is_valid_key(uid, guild)
        val = self.users[uid][guild]
        self.users[uid][guild] = val + int(random.randint(1,10))
        return self.users[uid][guild]
    

    def add_to_set(self, uid:hikari.snowflakes.Snowflake, guild:hikari.snowflakes.Snowflake) -> int:
        if not self.guild_users_chatted_map.get(guild):
           self.guild_users_chatted_map[guild] = set()
        self.guild_users_chatted_map[guild].add(uid)

    