import disnake
from disnake.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='help', description='Shows all commands!')
    async def Help(inter):
        msg = "your-commands-list"
        await inter.response.send_message(msg)
            
def setup(bot):
    bot.add_cog(Help(bot))