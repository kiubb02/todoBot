import discord
from discord.ext import commands
from random import randint
import datetime, asyncio

# BOT THAT CREATES A TODO MAP BASED ON SUBJECT AND EVERYTJHING

TOKEN = "MTAwNjE0NzQ4NzI3MjI3MTkxMg.GrYIj0.FFMDP9dtveblUVQ91-MGmDyqSdqqOXe3XmyD_8"

client = discord.Client()
bot = commands.Bot(command_prefix="!")

todoList = []


@bot.command()
async def showall(ctx):
    await ctx.send(todoList)


@bot.command()
async def add():
    await ctx.send(todoList)


@bot.command()
async def delete():
    await ctx.send()


bot.run(TOKEN)
