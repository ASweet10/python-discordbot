import os
import datetime
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import tasks
from responses import get_response

# Setup
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)



async def send_message(message, user_message):
    if not user_message:
        print('(Message was empty)')
        return
    
    is_private = user_message[0] == '?' # If first message is question mark, make private

    if is_private:
        user_message = user_message[1:] # Slice user message from 1 onward

    try:
        response = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# Startup
@client.event
async def on_ready():
    print(f'{client.user} is now running')
    WishMerryChristmas.start()


# Handle incoming messages
@client.event
async def on_message(message):
    if message.author == client.user: # if bot wrote message
        return 
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


today = datetime.date.today()
christmasTime = datetime.date(today.year, 12, 25)

@tasks.loop(time=christmasTime)
async def WishMerryChristmas():
    channel = client.get_channel(1332749239364616300)
    await channel.send("Ho ho ho! Merry Christmas! Bah Humbug.")


now = datetime.datetime.now()
bedTime = datetime.time(22, 0, 0, 0)

@tasks.loop(time=bedTime)
async def WishGoodnight():
    channel = client.get_channel(1332749239364616300)
    await channel.send("Nighty night don't let the bedbugs bite")

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()