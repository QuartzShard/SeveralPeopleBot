## Initialization
import discord
from discord.ext import commands, tasks

## General utility commands
class typing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ## Type!
    @commands.Cog.listener()
    async def on_message(self, ctx):
        await ctx.channel.trigger_typing()
    
    @commands.command()
    async def callout(self, ctx):
        embed = self.embedMessage.embed(
            title = f'twitter.com: @{self.bot.user.display_name} updated their status',
            description = f'***I\'ve come to make an announcement: {ctx.author.mention}\'s a bitch-ass motherfucker. He pissed on my fucking wife. That\'s right, he took his hedgehog fuckin\' quilly dick out and he pissed on my fucking wife, and he said his dick was \"THIS BIG\", and I said \"That\'s disgusting!\" So I\'m making a callout post on my Twitter dot com. {ctx.author.mention}, you got a small dick! It\'s the size of this walnut except WAY smaller! And guess what? Here\'s what my dong looks like! That\'s right, baby! All points, no quills, no pillows, look at that, it looks like two balls and a bong! He fucked my wife, so guess what, I\'m gonna fuck the Earth! That\'s right, this is what you get, my SUPER LASER PISS! Except I\'m not gonna piss on the Earth, I\'m gonna go higher. I\'m pissing on the MOON! HOW DO YOU LIKE THAT, OBAMA? I PISSED ON THE MOON, YOU IDIOT!  You have 23 hours before the piss DRRRROPLLLETS hit the fucking Earth! Now get out of my fucking sight, before I piss on you too!***',
            color = discord.Color.from_rgb(42, 169, 224)
        )
        await ctx.send(embed = embed)

    ## Helper function for using message embeds
    def embed(self, **kwargs):
        """
        Created an embed from the provided details
        title - Title of embed
        description - Text in embed, pre body
        sections - list of (title,content) tuples
        body - list of entries to be seperated by a <hr>, follows sections
        colour - discord.Colour object to ovveride default
        url - webpage to link to
        thumbnail - boolean to display roleman thumbnail
        footer - Text to put at the bottom of the embed
        """
        
        embed=Embed()
    
        ## Check for present kwargs and edit embed accordingly
        if ("title" in kwargs.keys()):
            embed.title = kwargs["title"]
        if ("description" in kwargs.keys()):
            embed.description = kwargs["description"]
        if ("sections" in kwargs.keys()):
            for elem in kwargs["sections"]:
                embed.add_field(name=elem[0],value=elem[1])
        if ("body" in kwargs.keys()):
            for elem in kwargs["body"]:
                embed.add_field(name=hr,value=elem, inline=False)
            #now = datetime.datetime.now().strftime("%H:%M")
            #embed.add_field(name=hr,value=f"Request fulfilled at {now}",inline=False)
        if ("colour" in kwargs.keys()):
            embed.colour = kwargs["colour"]
        elif ("color" in kwargs.keys()):
            embed.color = kwargs["color"] 
        else:
            embed.colour = defaultColour
        if ("url" in kwargs.keys()):
            embed.url = kwargs["url"]
        if ("thumbnail" in kwargs.keys()):
            if kwargs["thumbnail"]:
                embed.set_image(url=cfg['options']['embed']['thumbnail'])
        if ("footer" in kwargs.keys()):
            embed.set_footer(text=kwargs["footer"])
        return embed
    
## Allow use of cog class by main bot instance
def setup(bot):
    bot.add_cog(typing(bot))
