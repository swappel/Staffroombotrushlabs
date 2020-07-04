import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('mit Mitarbeitern'), status=discord.Status.do_not_disturb)


@bot.command()
async def flitzeauto(ctx):
    await ctx.send('Flitzflitzbrummmmmmmbrummmmmmmmmwrumbumpum!!!')


client.run('process.enc.BOT_TOKEN');
