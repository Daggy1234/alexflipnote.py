# alexflipnote.py
 An easy to use Python Wrapper for the AlexFlipnote API

# installation
> pip install alexflipnote.py

# Examples

### Get a random cat pic:

```py
import alexflipnote

afa = alexflipnote.Client()

print(await afa.cats)
>>> https://api.alexflipnote.dev/cats/grRlHyi-AL8_cats.jpg
``` 

### Get supreme logo
```py
import alexflipnote

afa = alexflipnoteClient()

print(await afa.supreme("#some text, yes", dark=True)) # making it dark, there is also light = True.
>>> https://api.alexflipnote.dev/supreme?text=%23some%20text,%20yes&dark=true
``` 

### Color info command in a discord.py Bot:

```py
import alexflipnote
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
colour_api = alexflipnote.Client()

# source: https://github.com/AlexFlipnote/discord_bot.py/blob/6d1adc72e9c19bb4ca90718e5f6d335faf842dd9/cogs/fun.py#L114-L147

@bot.command(aliases=['color'])
async def colourinfo(ctx, colour: str)):
    """ View the colour HEX details """
    async with ctx.channel.typing():
        if not permissions.can_embed(ctx):
            return await ctx.send("I can't embed in this channel ;-;")

        if colour[:1] == "#":
            colour = colour[1:]

        try:
            if color.lower() == "random":
                get_colour = await color_api.colour() # random color
            get_colour = await color_api.colour(colour)
        except ap.BadRequest as e: # if not valid HEX
            return await ctx.send(e)
        except aiohttp.ClientConnectorError:
            return await ctx.send("The API seems to be down...")
        except aiohttp.ContentTypeError:
            return await ctx.send("The API returned an error or didn't return JSON...")

        embed = discord.Embed(colour=get_colour.int)
        embed.set_thumbnail(url=get_colour.image)
        embed.set_image(url=get_colour.image_gradient)

        embed.add_field(name="HEX", value=get_colour.hex, inline=True)
        embed.add_field(name="RGB", value=get_colour.rgb, inline=True)
        embed.add_field(name="Int", value=get_colour.int, inline=True)
        embed.add_field(name="Brightness", value=get_colour.brightness, inline=True)

        await ctx.send(embed=embed, content=f"{ctx.invoked_with.title()} name: **{get_colour.name}**")
```

# Made by

This wrapper is made Soheab_#6240, contact me for anything related to this wrapper.

This was made for the AlexFlipnote api. Link: https://api.alexflipnote.dev.
