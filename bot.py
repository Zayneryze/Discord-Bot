import discord
from discord.ext import commands
from colorama import Back, Fore, Style
import time
import platform
import os
import random
import asyncio
import json
from datetime import date

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@client.event
async def on_ready():
  prfx = (Back.BLACK + Fore.GREEN +time.strftime("%H:%M:%S UTC ", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
  print(prfx + "Logged in as " + Fore.YELLOW + client.user.name)
  print(prfx + "BOT ID " + Fore.YELLOW + str(client.user.id))
  print(prfx + "Discord Version " + Fore.YELLOW + discord.__version__)
  print(prfx + "Python Version " + Fore.YELLOW +
        str(platform.python_version()))





@client.command(aliases=["close", "stop"])
async def shutdown(ctx):
  await ctx.send("Shutting down the bot.")
  await client.close()


@client.command(aliases=["dice"])
async def roll(ctx, max: int = 6):
  number = random.randint(1, max)
  await ctx.send(number)

@client.command(aliases=["choice"])
async def choose(ctx,*, args):
  arguments = args.split(" ")
  choice = random.choice(arguments)
  thinking = await ctx.send(":clock1: Thinking...")
  await asyncio.sleep(0,2)
  for i in range(12):
      await thinking.edit(content=f":clock{i+1}: Thinking...")
      await asyncio.sleep(0,2)
  await ctx.send(choice)


@client.command(aliases =["guessing"])
async def guess(ctx, max:int=10):
  real_number = random.randint(1,max)
  print(real_number)
  await ctx.send(f"Guessing game started!\nPlease guess a number between 1-{max} within **5** tries.")
  def check(m):
    return m.author == ctx.author and m.channel == ctx.message.channel
  for i in range(5):
    guess = await client.wait_for('message',check=check)
    if guess.content == str(real_number):
      await ctx.send(f"You guessed correctly, it took you **{i+1}** tries!")
    elif guess.content > str(real_number):
      await ctx.send("Lower!")
    elif guess.content < str(real_number):
      await ctx.send("Higher!")

  else:
      await ctx.send(f"Game Lost! The correct number was **{real_number}**. ")

@client.command()
async def monday(ctx):
  await ctx.send(":weary:")

@client.command()
async def tuesday(ctx):
  await ctx.send(":weary:")

@client.command()
async def wednesday(ctx):
  await ctx.send(":weary:")

@client.command()
async def thursday(ctx):
  await ctx.send(":weary:")

@client.command()
async def friday(ctx):
  await ctx.send(":weary:")

@client.command()
async def saturday(ctx):
  await ctx.send(":weary:")

@client.command()
async def sunday(ctx):
  await ctx.send(":weary:")

@client.command(aliases=["dates and day"])
async def dates(ctx):
  today_date = date.today()
  week_day = today_date.strftime('%A')
  await ctx.send(f"Today's date: {today_date}.\nThe day is {week_day}.")

  
  
  




  
  


client.run("MTA5MDU5MDM3ODMwMzk1OTA0MQ.Gn2AHb.FD_3-uem7M88nbGe8OA9D7Q-gUSJOoYapFZMJw")
