import discord
import foreground_editor as f
from discord.ext import commands


bot = commands.Bot(command_prefix="!", case_insensitive=True)
DISCORD_TOKEN='YOUR TOKEN HERE'
client = discord.Client()

    
@bot.command(name='hello', description="Greet the user!")
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!") 
@bot.command()
async def upload_file(ctx, arg1,arg2):
    print("argument recieved!")
    print(arg1)
    f.foreground_destroyer(arg1, int(arg2))
    await ctx.send(file=discord.File("deez.png"))
bot.run(DISCORD_TOKEN)
