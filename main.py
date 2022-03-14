
import json
import os
import random
import sys
import time
from ctypes import *
from datetime import datetime
from itertools import cycle
from random import choice, randint

import aiohttp

import disnake
from disnake import Embed, activity
from disnake import asset
from disnake.ext import *
from disnake.ext import commands, tasks
from disnake.ext.commands import *
from disnake.utils import find, get

import string


import inspect
import io
import textwrap
import traceback
import aiohttp
from contextlib import redirect_stdout











if os.path.exists(os.getcwd() + "/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]


intents = disnake.Intents.default()
intents.typing = False
intents.presences = False
# intents.members = True
intents.reactions = True


bot = commands.Bot(command_prefix="funneh-", intents=intents, activity=disnake.Activity(type=disnake.ActivityType.watching, name=f"commands"))
bot.remove_command('help')





if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"serverbanned": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

serverbanned = configData["serverbanned"]












if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"badList": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

badList = configData["badList"]












if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"theowners": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

theowners = configData["theowners"]









if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"thebot": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

thebot = configData["thebot"]











if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"custom_commands_server_ID": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

custom_commands_server_ID = configData["custom_commands_server_ID"]




















@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    print('Bot is starting..')
    print('------')
    print(f"disnake: {disnake.__version__}\n")








@bot.listen()
async def on_guild_join(guild):
    if guild.id in serverbanned:
        await guild.leave()


@bot.listen()
async def on_message(message):
    if message.guild.id in serverbanned:
        await message.guild.leave()



@bot.listen()
async def on_slash_command_error(inter, error):
    embed = disnake.Embed(title="A slash command error occured", color=0xD708CC, description=f"```{str(error)}```")      
    embed.timestamp = disnake.utils.utcnow() 
    await inter.response.send_message(embed=embed)


@bot.listen()
async def on_user_command_error(inter, error):
    embed = disnake.Embed(title="A user command error occured", color=0xD708CC, description=f"```{str(error)}```")      
    embed.timestamp = disnake.utils.utcnow() 
    await inter.response.send_message(embed=embed)

@bot.listen()
async def on_message_command_error(inter, error):
    embed = disnake.Embed(title="A message command error occured", color=0xD708CC, description=f"```{str(error)}```") 
    embed.timestamp = disnake.utils.utcnow() 
    await inter.response.send_message(embed=embed)







@bot.slash_command(name="easyguess", description="Guess a number between 1-10")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def easyguess(inter, number: int = Param(desc="The number")):

    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    if number>10:
        return await inter.response.send_message("You can't choose a number greater than 10!", ephemeral=True)

    if number<1:
        return await inter.response.send_message("Your number can not be below 0 or lower. The number must be between 1-10", ephemeral=True)

    answer = random.randint(1, 10)

    if number==answer:
        return await inter.response.send_message("You got it right!")


    else:
        await inter.response.send_message(f"Incorrect! The answer was {answer}")






@bot.slash_command(name="mediumguess", description="Guess a number between 1-50")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def mediumguess(inter, number: int = Param(desc="The number")):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    if number>50:
        return await inter.response.send_message("You can't choose a number greater than 50!", ephemeral=True)

    if number<1:
        return await inter.response.send_message("Your number can not be below 0 or lower. The number must be between 1-50", ephemeral=True)

    answer2 = random.randint(1, 50)

    if number==answer2:
        return await inter.response.send_message("You got it right!")


    else:
        await inter.response.send_message(f"Incorrect! The answer was {answer2}")






@bot.slash_command(name="hardguess", description="Guess a number between 1-100")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def hardguess(
    inter: disnake.ApplicationCommandInteraction, number: int = Param(desc="The number")):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    if number>100:
        return await inter.response.send_message("You can't choose a number greater than 100!", ephemeral=True)

    if number<1:
        return await inter.response.send_message("Your number can not be below 0 or lower. The number must be between 1-50", ephemeral=True)

    answer3 = random.randint(1, 100)

    if number==answer3:
        return await inter.response.send_message("You got it right!")


    else:
        await inter.response.send_message(f"Incorrect! The answer was {answer3}")






@bot.slash_command(name="clap", description="clap your hands")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def clap(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message(f":clap: :clap: If your happy and you know it clap you hands! :clap: :clap:")





@bot.slash_command(name="cry", description="Don't make me cry!")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def cry(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message(':sob: You made me cry! How could you! :sob:')







@bot.slash_command(name="yeet", description="YEETING")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def yeet(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('YEET MOMENT! *yeets my friend out of my house*')









@bot.slash_command(name="notpog", description="unpog a moment")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def notpog(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('THAT WAS SO NOT POGGERS!')










@bot.slash_command(name="fake_error", description="A fake error")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def fake_error(inter: disnake.ApplicationCommandInteraction):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    
        fake_errors = [ "Your mom has called you from school and found out you skipped school. Your video games have been destroyed. Go to your room and never come out child.",
                       "Discord has banned your account for spamming me with NSFW!",
                       "Discord.exe has stopped working.", "System32 has been stopped working, your computer files have been deleted.",
                       "You have been banned from using Funneh Bot#7790"
            
            
            
        ]
        response = random.choice(fake_errors)

        embed = disnake.Embed(title="A very imporant error has occured.", color=0xD708CC, description=f"```{response}```")      
        embed.timestamp = disnake.utils.utcnow() 
        await inter.response.send_message(embed=embed)












@bot.slash_command(name="eightball", description="An eightball command. test if you should do something.")
async def eightball(inter: disnake.ApplicationCommandInteraction, *, question):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass

        ballresponse = [
            "Yes", "No", "Take a wild guess...", "Very doubtful",
            "It is certain", "Without a doubt", "Most likely", "Yes, definitely", "Signs point to yes",
            "No", "My reply is no", "My sources say no", "Outlook not so good", "Don’t count on it", "Concentrate and ask again",
        ]

        response = random.choice(ballresponse)

        embed = disnake.Embed(title=f"🎱 Question: {question}", color=0xD708CC, description=f"")
        embed.set_footer(text=f"Your answer:  {response}")
        embed.timestamp = disnake.utils.utcnow() 
        await inter.response.send_message(embed=embed)



@bot.slash_command(name="bruh", description="this is a bruh moment")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def bruh(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('THIS IS SUCH A BRUH MOMENT!')





@bot.slash_command(name="owo", description="owo to uwu")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def owo(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('uwu')



@bot.slash_command(name="ip", description="Server ips")
@disnake.ext.commands.cooldown(7, 15, type=disnake.ext.commands.BucketType.user)
async def ip(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass


    if inter.guild.id in custom_commands_server_ID:
        await inter.response.send_message("The server IPs are in <#882012729827786762>")

    else:
        await inter.response.send_message("This is a custom command that can not be used in other servers!\nAuthor's ID of custom command owner: **513072262409355274**")



@bot.slash_command(name="uwu", description="uwu to owo")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def owo(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('owo')








@bot.slash_command(name="notping", description="this is fake ping")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def notping(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass

    fakeping = random.randint(5000000, 9999999999)

    await inter.response.send_message(f"Pong! {fakeping}")









@bot.slash_command(name="news", description="Information about User319183#3149")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def news(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('GUYS THIS IS IMPORTANT! **User319183#3149 HAS DIED!!** THIS IS TERRIBLE! WATCH HIS LAST VIDEO OF HIM SAYING GOODBYE! ||<https://www.youtube.com/watch?v=dQw4w9WgXcQ.>||')



@bot.slash_command(name="rate", description="Let Funneh Bot rate a member/bot")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def rate(inter, member: disnake.Member):

    
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass

    if member.id in thebot:
        await inter.response.send_message(f"I rate `myself` a **100 / 100** since I'm the best fun bot to be on Discord :sunglasses:")

    if member.id in theowners:
        await inter.response.send_message(f"I rate `User319183#3149` a **100 / 100** since he's the bot developer :sunglasses:")

    else:

        rate_amount = random.randint(0, 100)
        await inter.response.send_message(f"I rate `{member}` a **{round(rate_amount, 4)} / 100**")


@bot.slash_command(name="frick", description="Don't say it!")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def frick(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('Buddy, we both know what you were going to say...')







@bot.slash_command(name="tomato", description="tomato to tomoto")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def tomato(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('tomoto')







@bot.slash_command(name="tomoto", description="tomoto to tomato")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def tomoto(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('tomato')










@bot.slash_command(name="school", description="School sucks")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def school(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('LOOK, SCHOOL SUCKS. YOU REALLY WANT TO SIT THERE FOR 5-8 HOURS JUST LEARNING?!')











@bot.slash_command(name="oof", description="well oof")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def oof(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('OOF!')










@bot.slash_command(name="crash", description="crash the bot")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def crash(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('Shutting down bot forever... ||JUST KIDDING! do you hate me? Why do you want me to crash?!||')







@bot.slash_command(name="robux", description="Free robux")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def robux(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    await inter.response.send_message('Ah, I see you want free robux..I will give you it. Here is a free code: ||ᴳᴱᵀ ᴿᴵᑦᴷᴿᴼᴸᴸᴱᴰ||')





@bot.slash_command(name="randomfact", description="Get a free random fact.")
@disnake.ext.commands.cooldown(1, 10, type=disnake.ext.commands.BucketType.user)
async def randomfact(inter):

    # This will prevent your bot from stopping everything when doing a web request - see: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
    async with aiohttp.ClientSession() as session:
        async with session.get("https://uselessfacts.jsph.pl/random.json?language=en") as request:
            if request.status == 200:
                data = await request.json()
                embed = disnake.Embed(description=data["text"], color=0xD75BF4)
                await inter.response.send_message(embed=embed)
            else:
                embed = disnake.Embed(
                    title="Error!",
                    description="There is something wrong with the API, please try again later",
                    color=0xE02B2B
                )
                await inter.response.send_message(embed=embed)


@bot.user_command(name="Avatar")
@disnake.ext.commands.cooldown(1, 10, type=disnake.ext.commands.BucketType.user)
async def avatar(inter: disnake.UserCommandInteraction):

    if inter.guild is None:
        return await inter.response.send_message("User commands can't be used in DM's!")

    # inter.target is the user you clicked on
    emb = disnake.Embed(title=f"{inter.target}'s avatar")
    emb.set_image(url=inter.target.display_avatar.url)
    await inter.response.send_message(embed=emb)


    


@bot.user_command(name="Hug")
@disnake.ext.commands.cooldown(1, 5, type=disnake.ext.commands.BucketType.user)
async def hug(inter: disnake.UserCommandInteraction):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass

    if inter.guild is None:
        return await inter.response.send_message("User commands can't be used in DM's!")

    await inter.response.send_message(f"{inter.target} was hugged")


@bot.user_command(name="Fakeban")
@disnake.ext.commands.cooldown(1, 5, type=disnake.ext.commands.BucketType.user)
async def fakeban(inter: disnake.UserCommandInteraction):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass

    if inter.guild is None:
        return await inter.response.send_message("User commands can't be used in DM's!")

    await inter.response.send_message(f"{inter.target} has been struck by the ban hammer.")


@bot.user_command(name="slap")
@disnake.ext.commands.cooldown(1, 5, type=disnake.ext.commands.BucketType.user)
async def slap(inter: disnake.UserCommandInteraction):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass

    if inter.guild is None:
        return await inter.response.send_message("User commands can't be used in DM's!")

    slapresponses = [
        "with a fish", "by his dog", "by his cat", "by Funneh Bot",
        f"by {inter.author}"
    ]

    slapresponses = random.choice(slapresponses)

    await inter.response.send_message(f"{inter.target} has been slapped **{slapresponses}**.")







@bot.user_command(name="kill")
@disnake.ext.commands.cooldown(1, 5, type=disnake.ext.commands.BucketType.user)
async def kill(inter: disnake.UserCommandInteraction):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass

    if inter.guild is None:
        return await inter.response.send_message("User commands can't be used in DM's!")

    killresponses = [
        "by watching Power Rangers", "by a computer", "by being on Discord for so long", "by Funneh Bot",
        "by eating Sour Patch"
    ]

    killresponse = random.choice(killresponses)
        
    await inter.response.send_message(f'{inter.target} has been killed **{killresponse}**.')




#help panel


# Defines a simple view of buttons for the embed.
class Menu(disnake.ui.View):
    

    def __init__(self, embeds: list[disnake.Embed]):
        super().__init__(timeout=60)
        
        # Sets the embed list variable.
        self.embeds = embeds

        # Current embed number.
        self.embed_count = 0

    @disnake.ui.button(label="Previous page", emoji="◀️", style=disnake.ButtonStyle.red)
    async def next_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.embed_count == 0: # If current embed is the first embed then, do not do anything.
            pass
        else: # If current embed is not the first embed then, sends the preview embed.
            self.embed_count -= 1

            # Gets the embed object.
            embed = self.embeds[self.embed_count]

            # Sets the footer of the embed with current page and then sends it.
            embed.set_footer(text=f"Page {self.embed_count + 1} of {len(self.embeds)}")
            await interaction.response.edit_message(embed=embed)

    @disnake.ui.button(label="Next page", emoji="▶️", style=disnake.ButtonStyle.green)
    async def last_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.embed_count == (len(self.embeds) - 1): # If current embed is the last embed then, do not do anything.
            pass
        else: # If current embed is not the last embed then, sends the next embed.
            self.embed_count += 1

            # Gets the embed object.
            embed = self.embeds[self.embed_count]

            # Sets the footer of the embed with current page and then sends it.
            embed.set_footer(text=f"Page {self.embed_count + 1} of {len(self.embeds)}")
            await interaction.response.edit_message(embed=embed)






@bot.slash_command(name="help", description="The help panel")
@disnake.ext.commands.cooldown(1, 10, type=disnake.ext.commands.BucketType.user)
async def help(inter):


    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass



    # Creates the embeds as a list.
    embeds = [
        disnake.Embed(title="Support Server:", description="https://discord.gg/ecz2z36gkB", colour=disnake.Colour.random()),
        disnake.Embed(title="Fun Section:", description=" \n vbucks \n roast \n nitro \n rate \n eightball \n fake_error \n bruh \n clap \n crash \n cry \n frick \n news \n notping \n notpog \n oof \n owo \n school \n tomato \n tomoto \n uwu \n yeet \n easyguess \n mediumguess \nhardguess", colour=disnake.Color.random()),
        disnake.Embed(title="User Commands:", description=" \n avatar \n hug \n slap \n fakeban \n kill", colour=disnake.Color.random()),
        disnake.Embed(title="Other commands:", description=" \n userinfo \n calculate \n color \n fact \n getpfp \n dog \n cat \n uptime \n info \n advertise \n webhookecho \n", colour=disnake.Color.random()),
        disnake.Embed(title="Message commands:", description=" \n message_pog \n message_sucks \n funny \n unfunny \n", colour=disnake.Color.random()),
        disnake.Embed(title="Custom commands:", description=" \n ip", colour=disnake.Color.random()),
        
    ]

    # Sets the footer of the first embed.
    embeds[0].set_footer(text=f"Page 1 of {len(embeds)}")

    # Sends first embed with the buttons, it also passes the embeds list into the View class.

    await inter.response.send_message(embed=embeds[0], view=Menu(embeds))










#userecho
@bot.slash_command(name="webhookecho", description="Impersonate yourself with a webhook.")
@disnake.ext.commands.cooldown(1, 120, type=disnake.ext.commands.BucketType.user)
@disnake.ext.commands.has_permissions(administrator=True)
async def webhookecho(
    inter: disnake.ApplicationCommandInteraction,
    content: str = Param(description="The message"),
):

    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass


    if inter.guild is None:
        return await inter.response.send_message("<:slash:782701715479724063> This slash command can't be used in DM's!")

    
    # We fetch the channel's webhooks.
    channel_webhooks = await inter.channel.webhooks()
    webhook_count = 0

    await inter.response.send_message(f"Slash webhook been sent {inter.author.mention}")

    # We check if the bot's webhook already exists in the channel.
    for webhook in channel_webhooks:
        # We will check if the creator of the webhook is the same as the bot, and if the name is the same.
        if webhook.user.id == bot.user.id and webhook.name == "Bot Webhook":
            await webhook.send(content=content, username=inter.author.display_name, avatar_url=inter.author.display_avatar.url)
            return # The program will not go further.
    
    # If the webhook does not exist, it will be created.
    new_webhook = await inter.channel.create_webhook(name="Bot Webhook", reason="Bot Webhook")
    await new_webhook.send(content=content, username=inter.author.display_name, avatar_url=inter.author.display_avatar.url)













class MySelect(disnake.ui.Select):
    def __init__(self):
        

        options = [
            disnake.SelectOption(
                label="Nitro", description="After clicking this select option you will be redirected.", emoji="😃"
            ),
        ]

        super().__init__(
            placeholder="Click this if you want nitro for free.",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        await interaction.response.send_message(content=f"{interaction.author.mention} https://imgur.com/CPLIwdO", ephemeral=True)

@bot.slash_command(name="nitro", description="Free Discord nitro!")
async def nitro(inter: disnake.ApplicationCommandInteraction):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass


    view = disnake.ui.View()
    view.add_item(MySelect())

    await inter.response.send_message(" https://dis.cord.gift/mycoolepicnitropleasehaha ", view=view)








@bot.slash_command(name="advertise", description="Some Simple command")
@disnake.ext.commands.has_permissions(administrator=True)

@disnake.ext.commands.cooldown(1, 604800, type=disnake.ext.commands.BucketType.guild)
async def advertise(inter, description: str = Param(desc="The server's description."),):

    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass

    if inter.guild is None:
        return await inter.response.send_message("<:slash:782701715479724063> This slash command can't be used in DM's!")

    invite = await inter.channel.create_invite()
    await inter.response.send_message("Your server has been advertised in the **Funneh Bot** support server.\n  Note: If you have not advertised with the correct description, please delete the invite I have created.")
    channel=bot.get_channel(888567793816043550)

    embed = disnake.Embed(title = "Server Advertised", description = "\u2800", color=0x009dff)
    embed.add_field(name = "Server Name:", value = f"{inter.guild.name}")
    embed.add_field(name = "Server Invite:", value = f"{invite}.")
    embed.add_field(name = "Author", value = f"{inter.author}")
    embed.add_field(name = "Description", value = f"{description}")
    await channel.send(embed=embed)



    chan=bot.get_channel(888567486402953266)

    embed = disnake.Embed(title = "Server Advertised", description = "A new server has been advertised.", color=0x009dff)
    embed.add_field(name = "Server Name:", value = f"{inter.guild.name}")
    embed.add_field(name = "Guild ID", value = f"{inter.guild.id}")
    embed.add_field(name = "Server Invite:", value = f"{invite}.")
    embed.add_field(name = "Author's ID", value = f"{inter.author.id}")
    embed.add_field(name = "Description", value = f"{description}")
    embed.add_field(name = "User Mention (if possible)", value=f"{inter.author.mention}")
    await chan.send(embed=embed)






@bot.slash_command(name="userinfo", description="Information about a user.")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def userinfo(inter, member: disnake.User = Param(default=lambda inter: inter.author),):
        
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass



    date_format = "%a, %d %b %Y %I:%M %p"
    embed = disnake.Embed(color=disnake.Color.blue(), description=member.mention)
    embed.set_author(name=str(member), icon_url=member.display_avatar.url)
    embed.set_thumbnail(url=member.display_avatar.url)

    


    try:

        embed.add_field(name="Joined", value=member.joined_at.strftime(date_format))

    except:
        pass
    
    embed.add_field(name="Registered", value=member.created_at.strftime(date_format))


    try:

        if len(member.roles) > 1:
            role_string = ' '.join([r.mention for r in member.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(member.roles)-1), value=role_string, inline=False)

    except:
        pass

    try:
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
        embed.add_field(name="Guild permissions", value=perm_string, inline=False)

    except:
        pass


    embed.add_field(name="Bot:", value=f"{member.bot}")
    embed.add_field(name="Discriminator:", value=f"{member.discriminator}")
    embed.add_field(name="Animated Profile Picture:", value=f"{member.display_avatar.is_animated()}")

    try:

        embed.add_field(name="Server Nickname:", value=f"{member.nick}")
        

    except:
        pass
    embed.set_footer(text='ID:' + str(member.id))
    await inter.response.send_message(embed=embed)
















@bot.listen()
async def on_guild_join(guild):
    channel = bot.get_channel(888567059762516028)

    total_users = len(guild.members)
    total_bots = len([member for member in guild.members if member.bot == True])
    total_humans = total_users - total_bots

    e = disnake.Embed(title="I've joined a server.", color= 3447003)
    e.add_field(name="Server Name:", value=guild.name, inline=False)
    e.add_field(name="Guild ID", value=guild.id, inline=False)
    e.add_field(name="Guild Owner", value=str(guild.owner), inline=False)
    e.add_field(name="Guild Users", value="{}".format(total_users))
    e.add_field(name="Humans", value=total_humans)
    e.add_field(name="Bots", value=total_bots)
    try:
        e.set_thumbnail(url=guild.icon.url)

    except:
        pass

    e.timestamp = datetime.datetime.utcnow()

    await channel.send(embed=e)





#find remove guild
@bot.listen()
async def on_guild_remove(guild):
    channel = bot.get_channel(888567083611332668)


    total_users = len(guild.members)
    total_bots = len([member for member in guild.members if member.bot == True])
    total_humans = total_users - total_bots

    e = disnake.Embed(title="I've left a server.", color=15158332)
    e.add_field(name="Server Name:", value=guild.name, inline=False)
    e.add_field(name="Guild ID", value=guild.id, inline=False)
    e.add_field(name="Guild Owner", value=str(guild.owner), inline=False)
    e.add_field(name="Guild Users", value="{}".format(total_users))
    e.add_field(name="Humans", value=total_humans)
    e.add_field(name="Bots", value=total_bots)
    try:
        e.set_thumbnail(url=guild.icon.url)

    except:
        pass

    e.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=e)
    
    
    
    
    



import requests

@bot.slash_command(name="cat", description="Random pictures of a cat.")
@disnake.ext.commands.cooldown(1, 10, type=disnake.ext.commands.BucketType.user)
async def cat(inter):

    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    cat = requests.get("https://api.thecatapi.com/v1/images/search")
    url = cat.json()[0]["url"]
    await inter.response.send_message(url)


@bot.slash_command(name="dog", description="Random pictures of a dog.")
@disnake.ext.commands.cooldown(1, 10, type=disnake.ext.commands.BucketType.user)
async def dog(inter):

    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    dog = requests.get("https://api.thedogapi.com/v1/images/search")
    url = dog.json()[0]["url"]
    await inter.response.send_message(url)






bot.launch_time = datetime.utcnow()

@bot.slash_command(name="uptime", description="Check the bot's uptime")

@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def uptime(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    await inter.response.send_message(f"I have been up for **{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s)**")






@bot.slash_command(name="info", description="Information about the bot.")
@disnake.ext.commands.cooldown(1, 3, type=disnake.ext.commands.BucketType.user)
async def info(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
        servers = str(len(inter.bot.guilds))
        ping = round(bot.latency * 1000 )
        channels = str(len(set(inter.bot.get_all_channels())))


        em = disnake.Embed(title = "Information", description = "Information about Funneh Bot", color=0x009dff)
        em.add_field(name="Server count", value=servers, inline=False)
        em.add_field(name="Amount of channels this bot can see (global)", value=channels, inline=False)
        em.add_field(name="Webhook latency", value=ping, inline=False)

        await inter.response.send_message(embed=em)





@bot.message_command(name="message_pog") # optional
@disnake.ext.commands.cooldown(1, 10, type=disnake.ext.commands.BucketType.user)
async def message_pog(inter: disnake.MessageCommandInteraction):


    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass



    if inter.guild is None:
        return await inter.response.send_message("<:slash:782701715479724063> This slash command can't be used in DM's!")


    await inter.response.send_message(f"Message **__{inter.target.content}__** is poggers!")


@bot.message_command(name="message_sucks") # optional
@disnake.ext.commands.cooldown(1, 10, type=disnake.ext.commands.BucketType.user)
async def message_sucks(inter: disnake.MessageCommandInteraction):


    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass



    if inter.guild is None:
        return await inter.response.send_message("<:slash:782701715479724063> This slash command can't be used in DM's!")


    await inter.response.send_message(f"Message **__{inter.target.content}__**  sucks!")











@bot.message_command(name="funny")
@disnake.ext.commands.cooldown(1, 10, type=disnake.ext.commands.BucketType.user)
async def funny(inter: disnake.MessageCommandInteraction):


    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass


    if inter.guild is None:
        return await inter.response.send_message("<:slash:782701715479724063> This slash command can't be used in DM's!")


    await inter.response.send_message(f"Message **__{inter.target.content}__** was funny!")













@bot.message_command(name="unfunny")
@disnake.ext.commands.cooldown(1, 10, type=disnake.ext.commands.BucketType.user)
async def unfunny(inter: disnake.MessageCommandInteraction):

    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass



    if inter.guild is None:
        return await inter.response.send_message("<:slash:782701715479724063> This slash command can't be used in DM's!")


    await inter.response.send_message(f"Message **__{inter.target.content}__** was not funny!")















@bot.slash_command(name="hack", description="Hack a member")
@disnake.ext.commands.cooldown(1, 15, type=disnake.ext.commands.BucketType.user)
async def hack(inter, member:disnake.Member):
    
        if inter.author.id in badList:
            return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
        else:
            pass

    
        
    
            hack_password = [
                "12345678", "thiskidsmomisgay", "298gayasf", "sussyidoot69",
                "ilovu", "Snapchat512", "ilovepoop", "eggmoafen", "umom",
                "12312343poop", "iHAVENOFRIENDS"
            ]

            hack_password = random.choice(hack_password)
            
            
            
            hack_email = [
                f"{member}eatspoop@daddy.com", f"{member}kisses_hismomma@iloveugmail.mwah", f"{member}isgay@stupid.com", f"{member}eatsBut@but.com",
            ]

            hack_email = random.choice(hack_email)
            
            
            
            hack_IP = [
                "69.69.69.69", "11.222.33.44", "99.99.69.96", "12.11.10.09",
            ]
            hack_IP = random.choice(hack_IP)
            
            
            phone_number = [
                "7326987369", "6349972135", "7392247836", "7326639815",
            ]
            phone_number = random.choice(phone_number)
            


            hack_roblox_account_password = [
                "iloveroblox2334", "gamer31773", "IWuVRoBux65", "RobloxMommy", "RobloxKarren", "DavidUmomma", "daddy_gimmie_my_robux",
                "10krobux32", "banned123", "WeeWeePooPoo", "peepoopeepoo", "i_have_a_roblox_girlfriend69", "dragon", "FrEeRObXx", "1234567890", "EpicRobloxGamer"
            ]
            hack_roblox_account_password = random.choice(hack_roblox_account_password)
            
            
            
            hack_fortnite_account_password = [
                "RyZe", "not_tfue", "NINJAFAN", "Toxic_Sweat", "NRG_benjyfishy", "SnipeHype", "TTV'GAMER",
                "DaddyChill101", "IT_ME_MaRiO", "Just_Better_Than_u", "i_bad_at_thisgame", "TaketheLstupids"
            ]
            hack_fortnite_account_password = random.choice(hack_fortnite_account_password)
            
            
            member_2FA =[
                "True", "False"
            ]
            member_2FA = random.choice(member_2FA)
            
                
            await inter.response.send_message(f"Hacking **{member}**.")
            time.sleep(4)
            await inter.edit_original_message(content= f" **10% complete** Accessing ** {member} **'s Discord login.")
            time.sleep(4)
            await inter.edit_original_message(content= f"**18.23% complete** 2FA has been bypassed. \nEmail: **{hack_email}** \nPassword: **{hack_password}** \n ")
            time.sleep(5)
            await inter.edit_original_message(content= f" **25.32% complete** Accessing ** {member} **'s IP address.")
            time.sleep(5)
            await inter.edit_original_message(content= f" **34% complete** IP address: **{hack_IP}**")
            time.sleep(4)
            await inter.edit_original_message(content= f" **43.70% complete** Reported ** {member} **'s Discord account for breaking the Discord ToS. ")
            time.sleep(5)
            await inter.edit_original_message(content= f" **50% complete** Hacking ** {member} **'s phone.")
            time.sleep(4)
            await inter.edit_original_message(content= f"**57.76% Phone number: **{phone_number} ")
            time.sleep(5)
            await inter.edit_original_message(content= f" **65% complete** Breaching... ** {member} **'s roblox account. ")
            time.sleep(4)
            await inter.edit_original_message(content= f" **70.68% complete** Breach completed. Email: **{hack_email}**\nPassword: ** {hack_roblox_account_password} **")
            time.sleep(5)
            await inter.edit_original_message(content= f" **78% complete** Hacking **{member}**'s fortnite account.")
            time.sleep(5)
            await inter.edit_original_message(content= f" **85% complete** Attempting to bypass 2FA on **{member}**'s fortnite account.")
            
            if member_2FA == "True":
                time.sleep(5)
                await inter.edit_original_message(content= f" **94% complete** 2FA has been successfully bypassed on **{member}**'s fortnite account.")
                time.sleep(4)
                await inter.edit_original_message(content= f" **100% complete** Email: **{hack_email}**\nPassword: ** {hack_roblox_account_password} **")
                time.sleep(5)
                await inter.edit_original_message(content= f"**{member}**'s account has been successfully hacked. The hacks have finished.")
                
                
            else:
                await inter.edit_original_message(content= f" **94% complete** 2FA couldn't be bypassed on **{member}**'s fortnite account. Accessing email and password instead.")     
                time.sleep(4)
                await inter.edit_original_message(content= f" **100% complete** Email: **{hack_email}**\nPassword: ** {hack_roblox_account_password} **")
                time.sleep(5)
                await inter.edit_original_message(content= f"**{member}**'s account has been successfully hacked. The hacks have finished.")
                
                    


from disnake.enums import ButtonStyle


class row_buttons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=60)



    # Creates a row of buttons and when one of them is pressed, it will send a message with the number of the button.

    @disnake.ui.button(label="Red", style=ButtonStyle.red)
    async def first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("Your favorite color is **Red** !", ephemeral=True)

    @disnake.ui.button(label="blue", style=ButtonStyle.blurple)
    async def second_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("Your favorite color is **Blue** !", ephemeral=True)

    @disnake.ui.button(label="pink", style=ButtonStyle.grey)
    async def third_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("Your favorite color is **Pink** !", ephemeral=True)

    @disnake.ui.button(label="purple.", style=ButtonStyle.blurple)
    async def fourth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("Your favorite color is **Purple** !", ephemeral=True)

    @disnake.ui.button(label="green", style=ButtonStyle.green)
    async def fifth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("Your favorite color is **Green** !", ephemeral=True)


@bot.slash_command(name="color", description = "Choose your favorite colors!")
async def color(inter):

    # Sends a message with a row of buttons.
    await inter.response.send_message("Choose your favorite color!", view=row_buttons(), ephemeral=True)








@bot.slash_command(name="roast", description="Roast a member")
async def roast(inter, member:disnake.Member):
    response = requests.get(url="https://evilinsult.com/generate_insult.php?lang=en&type=json")
    roast = json.loads(response.text)
    newroast=roast['insult']
    await inter.response.send_message(f"{member} this roast is for you: **{newroast}**")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
from simpcalc import simpcalc # pip install simpcalci


class InteractiveView(disnake.ui.View):
    def __init__(self, author):
        super().__init__()
        self.expr = ""
        self.calc = simpcalc.Calculate() # if you are using the above function, no need to declare this!
        self.author = author

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="1", row=0)
    async def one(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "1"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="2", row=0)
    async def two(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "2"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="3", row=0)
    async def three(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "3"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.green, label="+", row=0)
    async def plus(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "+"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="4", row=1)
    async def last(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "4"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="5", row=1)
    async def five(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "5"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="6", row=1)
    async def six(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "6"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.green, label="/", row=1)
    async def divide(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "/"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="7", row=2)
    async def seven(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "7"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="8", row=2)
    async def eight(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "8"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="9", row=2)
    async def nine(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "9"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.green, label="*", row=2)
    async def multiply(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "*"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, label=".", row=3)
    async def dot(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "."
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="0", row=3)
    async def zero(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "0"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.green, label="=", row=3)
    async def equal(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            try:
                self.expr = await self.calc.calculate(self.expr)
            except errors.BadArgument: # if you are function only, change this to BadArgument
                return await interaction.response.send_message("Please enter what I need to calculate!")
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.green, label="-", row=3)
    async def minus(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "-"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.green, label="(", row=4)
    async def left_bracket(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += "("
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.green, label=")", row=4)
    async def right_bracket(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr += ")"
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.red, label="CLEAR", row=4)
    async def clear(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr = ""
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.red, label="DEL", row=4)
    async def back(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if interaction.author == self.author:
            self.expr = self.expr[:-1]
            await interaction.message.edit(content=f"```\n{self.expr}\n```")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)
        

@bot.slash_command(name="calculate", description="Calculate an equation")
async def calculate(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    view = InteractiveView(inter.author)
    await inter.response.send_message("```\n```", view=view)
























class CoinFlip(disnake.ui.View):
    def __init__(self, author):
        super().__init__()
        self.author = author

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="Click the button to know your answer!", row=0)
    async def flip(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        responses = ['Heads!',
                    'Tails!']
        if interaction.author == self.author:

            await interaction.message.edit(content=f"{random.choice(responses)}")
        else:
            await interaction.response.send_message("You are not the author of this command!", ephemeral=True)



        

@bot.slash_command(name="coinflip", description="Flip a coin")
async def coinflip(inter):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    view = CoinFlip(inter.author)
    await inter.response.send_message("Heads or Tails?", view=view)













@bot.slash_command(name = "create_embed", description = "Create your own Discord embed!")
async def create_embed(inter, title = None, description = None, color = None, image_url = None, footer = None, footer_url = None):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    if color is not None:
        try:
            color = await commands.ColorConverter().convert(inter, color)
        except:
            color = disnake.Color.default()
    else:
        color = disnake.Color.default()
    reply = disnake.Embed(color=color)
    if title is not None:
        reply.title = title
    if description is not None:
        reply.description = description
    if image_url is not None:
        reply.set_image(url=image_url)
    pl = {}
    if footer is not None:
        pl['text'] = footer
    if footer_url is not None:
        pl['icon_url'] = footer_url
    if len(pl) > 0:
        reply.set_footer(**pl)
    await inter.response.send_message(embed=reply)

























memelist = ["dankmemes", "memes" "memers"]

@bot.slash_command(name="meme", description="Random memes")
@disnake.ext.commands.cooldown(1, 5, type=disnake.ext.commands.BucketType.user)
async def meme(inter: disnake.ApplicationCommandInteraction):
    if inter.author.id in badList:
        return await inter.response.send_message("You have been banned from doing this command!", ephemeral=True)
    else:
        pass
    try:
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
        async with aiohttp.ClientSession() as cs:
            mhemhe = random.choice(memelist)
            async with cs.get(f'https://www.reddit.com/r/{mhemhe}/new.json?sort=hot', headers={"user-agent": ran}) as r:
                res = await r.json()
                gg = random.randint(0, 25)
                title = res['data']['children'] [gg]['data']['title']
                author = f"u/{res['data']['children'] [gg]['data']['author']}"
                subreddit = res['data']['children'] [gg]['data']['subreddit_name_prefixed']
                upvotes = res['data']['children'] [gg]['data']['ups']
                image_url = res['data']['children'] [gg]['data']['url']
                post_url = f"https://reddit.com{res['data']['children'] [gg]['data']['permalink']}"
                embed = disnake.Embed(title="", description=f"__Author__ - `{author}`\n__Subreddit__ - `{subreddit}`\n[Click Here To Go To The Post]({post_url})")
                embed.set_author(name=title)
                embed.set_image(url=image_url)
                embed.set_footer(text=f"👍 (upvotes) - {upvotes}")
                await inter.response.send_message(embed=embed)
    
    except:
        pass




















#leave a server
@bot.command()
@commands.is_owner()
async def leave(ctx, guild_id):
    await bot.get_guild(int(guild_id)).leave()
    await ctx.send(f"I left the given server.")


#eval
@bot.command()
@commands.is_owner()
async def eval(ctx, *, body):
    """Evaluates python code"""
    env = {
        'ctx': ctx,
        'bot': bot,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
        'source': inspect.getsource
    }

    def cleanup_code(content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    def get_syntax_error(e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()
    err = out = None

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    def paginate(text: str):
        '''Simple generator that paginates text.'''
        last = 0
        pages = []
        for curr in range(0, len(text)):
            if curr % 1980 == 0:
                pages.append(text[last:curr])
                last = curr
                appd_index = curr
        if appd_index != len(text)-1:
            pages.append(text[last:curr])
        return list(filter(lambda a: a != '', pages))
    
    try:
        exec(to_compile, env)
    except Exception as e:
        err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        return await ctx.message.add_reaction('\u2049')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        if ret is None:
            if value:
                try:
                    
                    out = await ctx.send(f'```py\n{value}\n```')
                except:
                    paginated_text = paginate(value)
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')
        else:
            try:
                out = await ctx.send(f'```py\n{value}{ret}\n```')
            except:
                paginated_text = paginate(f"{value}{ret}")
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        out = await ctx.send(f'```py\n{page}\n```')
                        break
                    await ctx.send(f'```py\n{page}\n```')

    if out:
        await ctx.message.add_reaction('\u2705')  # tick
    elif err:
        await ctx.message.add_reaction('❌')  # x
    else:
        await ctx.message.add_reaction('\u2705')





























@bot.command()
async def stats(ctx):
    all_members_embed_list = []

    for x in bot.get_all_members():
        all_members_embed_list.append(x)

    print(f'{len(all_members_embed_list)}')





    
    
    
bot.run(token)
