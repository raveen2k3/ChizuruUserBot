from pyrogram import *
import os
from pyrogram.types import *
import asyncio
from pyrogram.types.messages_and_media import photo
from config import *
import config
import time , datetime
import random
from sys import version_info
import cowsay
from pyrogram import __version__ as pyro_version
from pySmartDL import SmartDL
from time import sleep
import requests

Mai = Client(
    session_name= config.SESSION_NAME,
    api_id=config.API_ID,
    api_hash=config.API_HASH ,
    bot_token=config.BOT_TOKEN,
)


owner_id = [1871813121]

prefixes=["." , "!"]

python_version = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"

@Mai.on_message(filters.command(["ping"] , prefixes))
async def ping (client , message):
    user_id = message.from_user.id
    if user_id in owner_id:
        chat_id = message.chat.id
        await message.edit("pong: " + str(random.randint(10 , 100)) + "ms")
        
BOT_VERSION = "0.2"
alive_msg = f"""

**WEEB USERBOT is Alive & Running**
    
    **Python Version:** `{python_version}`
    **Pyrogram Version:** `{pyro_version}`
    **Bot Version:** `{BOT_VERSION}`
**\n\n GET YOUR OWN TEST VERSION BY SPAMMING @its_raveen**"""



@Mai.on_message(filters.command(["alive"] , prefixes))
async def alive (client , message):
    user_id = message.from_user.id
    if user_id in owner_id:
        chat_id = message.chat.id
        #picyy = await Mai.get_profile_photos(user_id, limit=1)
        #pic = await Mai.download_media(picyy)
        pic = f"/home/raveen/Desktop/programming/private-main/RavenUserBot/components/kaguya.jpg"
        await Mai.delete_messages(chat_id , message.message_id)
        await Mai.send_photo(chat_id , photo= pic , caption= alive_msg)
        
@Mai.on_message(filters.command(["neko"], prefixes))
async def anime (client , message):
    user_id = message.from_user.id
    if user_id in owner_id:
        chat_id = message.chat.id
        r = requests.get(url = 'https://api.waifu.pics/sfw/neko')
        data = r.json()
        print(data)
        print(type(data))
        await Mai.delete_messages(chat_id , message.message_id)
        #await message.reply(data['url'])
        url = data['url']
        desti = f"/home/raveen/Desktop/programming/private-main/RavenUserBot/dlstuffs"
        obj = SmartDL(url, desti)
        obj.start()
        filename = path = obj.get_dest()
        await Mai.send_photo(chat_id , filename )
        sleep(5)
        await os.remove(desti)

abuse1 = "சேதபயலே நரபடலே பேதிலபிவான் அறுத்து கிளிச்சுடுவேன் மூஞ்சியும் மோகரையும் பாரு" 

abuse2 = "***tha  veliya jaaav"

abuse3 = " unnakulam vekka maanam soodu sorana la illaya da "

abuse4 = "vaaya moodra sanghi payya "

abuser = [abuse1 , abuse2 , abuse3 , abuse4]
@Mai.on_message(filters.command(["abuse"], prefixes))
async def alive(client , message):
    user_id = message.from_user.id
    if user_id in owner_id:
        try:
            target = message.reply_to_message.from_user.username

            if target:

            
                await message.edit(random.choice(abuser)+ " " +"@"+target)
            

        except Exception as e:
                        await message.edit(f"**REPLY TO A USER TO ABUSE** \n\n **ERROR:** - `{e}`")


@Mai.on_message(filters.command(["cowsay"], prefixes))
async def moo(client , message):
    user_id = message.from_user.id
    if user_id in owner_id:
        msg = message.text
        msg1 = msg.split(' ')[1]
        cow_text = str(msg1)
        final_cow = cowsay.get_output_string('cow', cow_text)
        Mai.set_parse_mode("markdown")
        await message.edit(final_cow , "**markdown** and <i>html</i>" )
        
@Mai.on_message(filters.command(["cat"], prefixes))
async def cat(client , message):
    try:
        user_id = message.from_user.id
        if user_id in owner_id:
            msg = message.text
            chat_id = message.chat.id
            msg1 = msg.split(' ')[1]
            catty = int(msg1)
            print(catty)
            await message.edit("Searching For your cat")
            url =f"https://http.cat/{catty}.jpg"
            print(url)
            desti = f"/home/raveen/Desktop/programming/private-main/RavenUserBot/dlstuffs"
            obj = SmartDL(url, desti)
            obj.start()
            filename = path = obj.get_dest()
            await client.delete_messages(chat_id , message.message_id)
            await client.send_photo(chat_id , photo=filename)
            await os.remove(desti)
    except:
        message.edit("GIVE A CORRECT A HTTP CODE TO FIND CAT")

@Mai.on_message(filters.command(["pin"], prefixes))
async def pin (client ,message):
    try:
            
        user_id = message.from_user.id
        if user_id in owner_id:
                chat_id = message.chat.id
                message_id = message.reply_to_message.message_id
                await Mai.pin_chat_message(chat_id, message_id)
                await message.edit("pinned succesfully")
                sleep(5)
                await Mai.delete_messages(chat_id , message.message_id)
    except:
        await message.edit("You are not admeme or you missed to reply a message master!!!")
        sleep(5)
        await Mai.delete_messages(chat_id , message.message_id)


    


        







        


Mai.run()






