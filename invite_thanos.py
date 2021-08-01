import discord
from discord import *
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
from discord import *
import asyncio

bot_token = "YOUR_DISCORD_BOT_TOKEN_HERE"
bot_prefix = "!"
minimum_invite_uses = 10

Client = discord.Client()
bot = commands.Bot(command_prefix = bot_prefix, case_insensitive=True)

@bot.event
async def on_ready():
      print(f"Bot Started... You can now clear invites below {minimum_invite_uses} uses with '{bot_prefix}purgeInvites'")

@commands.has_permissions(administrator=True)
@bot.command()
async def purgeInvites(ctx):
      await ctx.reply("Loading... (This part takes some time, get some coffee.)")
      invite_count = 0
      for channel in ctx.guild.channels:
            try:
                  for invite in (await channel.invites()):
                        invite_count += 1
            except:
                  pass
      await ctx.reply(f"**{ len(ctx.guild.channels)}** channels found, with a total of **{invite_count}** invites.")
      invite_deletion_count = 0
      for channel in ctx.guild.channels:
            try:
                  for invite in (await channel.invites()):
                        if (invite.uses) < minimum_invite_uses:
                              await invite.delete(reason=f"Thanos Snapped as it had below {minimum_invite_uses} total uses.")
                              invite_deletion_count += 1
            except:
                  pass
      await ctx.reply(f"**{invite_deletion_count}** invites deleted as they had below {minimum_invite_uses} uses.")

@bot.event
async def on_command_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
            await ctx.reply(f"{ctx.author.name}, you need to be an **admin** to run that command!")
      else:
            print(error) 

bot.run(bot_token)