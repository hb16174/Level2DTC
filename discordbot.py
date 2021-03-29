import discord
import random

client = discord.Client()

names = ['word']
add = ">Add"
DS = ["For Testing Purposes", "Also For Testing Purposes", "Testing Purposes 3"]
text = ""


# @client.event
# async def on_ready():
#    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_ready():
    # Setting `Listening ` status
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="ASMR"))
    print("Connected")

    # Setting `Playing ` status
    # await client.change_presence(activity=discord.Game(name="Minecraft 2"))
    # Setting `Streaming ` status
    # await client.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
    # Setting `Watching ` status
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you sleep"))


@client.event
async def on_message(message):
    print("")
    print(message.channel, ":")
    print(message.author, ":", message.content)
    if message.author == client.user:
        return

    msg = message.content
    msglower = message.content.lower()
    name = ""
    if msglower.startswith('>add '):
        # name = name.replace(add, '')
        names.append(name.replace(add, ''))
        await message.channel.send("Added "+name+" to the game")
    if msglower.startswith('>remove'):
        name = name.replace(">remove", "")
        if name in names:
            names.remove(name)
        # send = "```" + DS[random.randrange(len(DS))] + "```"
        await message.channel.send()
    if msglower.startswith('>characters'):
        print("List Requested, characters: ", names)
        await message.channel.send(names)

    # if any(word in msg for word in trigger):
    # await message.channel.send("Hey I'm not a bot")


def main():
    client.run('ODIzMTE1NDAxODgxMDU5MzI4.YFcH9A._W-Ziw03qvPwlE0TuAHtGT99QkM')


main()
