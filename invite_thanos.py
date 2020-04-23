import discord
from discord import *
from discord.ext.commands import Bot
from discord.ext.commands import MemberConverter
from discord.ext import commands
from discord.ext import *
from discord import *

# extra imports
import asyncio
import time

bot_token = "YOUR_DISCORD_BOT_TOKEN_HERE"
bot_prefix = ["meg!"]

Client = discord.Client()
bot = commands.Bot(command_prefix = bot_prefix, case_insensitive=True)


@bot.event
async def on_ready():
      print("Bot Started...")

@commands.has_permissions(administrator=True)
@bot.command()
async def thanos(ctx):
      await ctx.send("Loading... (This part takes some time, get some coffee.)")
      channels_ = len(ctx.guild.channels)
      invites_ = 0
      for channel in ctx.guild.channels:
            try:
                  for invite in (await channel.invites()):
                        invites_ += 1
            except:
                  pass
      await ctx.send("**%s** channels found, with a total of **%s** invites." % (channels_, invites_))
      good_eggs = 0
      bad_eggs = 0
      for channel in ctx.guild.channels:
            try:
                  for invite in (await channel.invites()):
                        if (invite.uses) < 10:
                              await invite.delete(reason="Thanos Snapped as it had below 10 total uses.")
                              bad_eggs += 1
                        else:
                              good_eggs += 1
            except:
                  pass
      await ctx.send("**%s** invites deleted as they had below 10 uses." % (bad_eggs))

@bot.event #on_command_error_event
async def on_command_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
            string = ""
            for permission in list(error.missing_perms):
                string = str(string)+str(permission)+", "
            message = await ctx.send("%s, you're lacking the following permission(s) `%s`." % (ctx.author.name, string[0:((len(string))-2)]))
            await clean_general(ctx, message)
      else:
            print(error) 

bot.run(bot_token)
