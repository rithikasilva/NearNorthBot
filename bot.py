import discord
import random
import nndsbChecker
import chippewaChecker
import westferrisChecker
import config
from discord.ext import tasks

# Initialized Client
client = discord.Client()

# Initializes Admin User Identity
admin_user = config.admin_user

# Initializes General Help Message
help_message = 'Actions:\n\n' \
               '!checknndsbw - checks the NNDSB website for new information\n\n' \
               '!checknndsbf -  checks the NNDSB Facebook page for the latest post\n\n' \
               '!checkchippewaw - checks the Chippewa website for new information\n\n' \
               '!checkchippewaf - checks the Chippewa Facebook page for the latest post\n\n' \
               '!checkferrisw - checks the West Ferris website for new information\n\n' \
               '!checkferrisf - checks the West Ferris Facebook page for the latest post\n\n' \
               '-----------------------------------------------------\n' \

# Function that wraps desired text input into discord bot wrapper
def wrap_box(to_be_wrapped):
    return "```" + to_be_wrapped + "```"


# Function that repeats every 4 hours to check for news
@tasks.loop(hours=4)
async def mytask():

    # Ensures that the loop doesn't begin before the client is initialized
    await client.wait_until_ready()

    # Changes the bots presence in order to inform the users that the bot is searching for information
    await client.change_presence(activity=discord.Game('Reporting News....'))

    # Sets channel as specified channel ID
    channel = client.get_channel(config.nndsb_updates_channel)

    # Sets content as non-user check for NNDSB Website
    content = nndsbChecker.checkWebsite(False)
    # If there is content to display, display the content in the specified channel
    if content != False:
        await channel.send(wrap_box("NNDSB WEB START"))
        await channel.send(content)
        await channel.send(wrap_box("NNDSB WEB END"))

    # Sets content as non-user check for NNDSB Facebook
    content = nndsbChecker.checkFacebook(False)
    # If there is content to display, display the content in the specified channel
    if content != False:
        await channel.send(wrap_box("NNDSB FACEBOOK START"))
        await channel.send(content)
        await channel.send(wrap_box("NNDSB FACEBOOK END"))

    # Sets content as non-user check for Chippewa Web
    content = chippewaChecker.checkWebsite(False)
    # If there is content to display, display the content in the specified channel
    if content != False:
        await channel.send(wrap_box("CHIPPEWA WEB START"))
        await channel.send(content)
        await channel.send(wrap_box("CHIPPEWA WEB END"))

    # Sets content as non-user check for Chippewa Facebook
    content = chippewaChecker.checkFacebook(False)
    # If there is content to display, display the content in the specified channel
    if content != False:
        await channel.send(wrap_box("CHIPPEWA FACEBOOK START"))
        await channel.send(content)
        await channel.send(wrap_box("CHIPPEWA FACEBOOK END"))

    # Sets content as non-user check for West Ferris Web
    content = westferrisChecker.checkWebsite(False)
    # If there is content to display, display the content in the specified channel
    if content != False:
        await channel.send(wrap_box("WEST FERRIS WEB START"))
        await channel.send(content)
        await channel.send(wrap_box("WEST FERRIS WEB END"))

    # Sets content as non-user check for West Ferris Facebook
    content = westferrisChecker.checkFacebook(False)
    if content != False:
        # If there is content to display, display the content in the specified channel
        await channel.send(wrap_box("WEST FERRIS FACEBOOK START"))
        await channel.send(content)
        await channel.send(wrap_box("WEST FERRIS FACEBOOK END"))

    # Changes the presence of the bot back to waiting message
    await client.change_presence(activity=discord.Game('Waiting For News'))

# Function that prints information to the console when the client is ready
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Bot is ready.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Waiting For News'))


# Function that ensures that bot doesn't reply to itself
@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return


# Function that provides output based on user input
@client.event
async def on_message(message):

    # If the user asks for help, print the help message
    if message.content.startswith('!help'):
        await message.channel.send(wrap_box(help_message))

    # If the user asks to check the NNDSB website page, display the latest post
    elif message.content.startswith('!checknndsbw'):
        content = nndsbChecker.checkWebsite(True)
        await message.channel.send(content)

    # If the user asks to check the NNDSB Facebook page, display the latest post
    elif message.content.startswith('!checknndsbf'):
        content = nndsbChecker.checkFacebook(True)
        await message.channel.send(content)

    # If the user asks to check the Chippewa website page, display the latest post
    elif message.content.startswith('!checkchippewaw'):
        content = chippewaChecker.checkWebsite(True)
        await message.channel.send(content)

    # If the user asks to check the Chippewa Facebook page, display the latest post
    elif message.content.startswith('!checkchippewaf'):
        content = chippewaChecker.checkFacebook(True)
        await message.channel.send(content)

    # If the user asks to check the West Ferris website page, display the latest post
    elif message.content.startswith('!checkferrisw'):
        content = westferrisChecker.checkWebsite(True)
        await message.channel.send(content)

    # If the user asks to check the West Ferris Facebook page, display the latest post
    elif message.content.startswith('!checkferrisf'):
        content = westferrisChecker.checkFacebook(True)
        await message.channel.send(content)


# Start the four hour checks for news
mytask.start()
# Run the bot
client.run(config.bot_key)
