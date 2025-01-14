from disnake.ext import commands

class MessageListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.add_listener(self.on_message, 'on_message')

    async def on_message(self, message):
        pass
        # On_message event
        
def setup(bot):
    bot.add_cog(MessageListener(bot))