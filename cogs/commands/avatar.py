import disnake
from disnake.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="avatar", description="Отправляет аватарку пользователя!")
    async def avatar(inter, member: disnake.Member = None):
        user = member if member else inter.author

        embed = disnake.Embed(title=user.display_name, colour=disnake.Color(0xff003d))
        embed.set_image(url=user.avatar.url)
        
        await inter.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Avatar(bot))