#    Copyright (c) 2021 Infinity BOTs <https://t.me/Infinity_BOTs>
 
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.

import os
import re
import requests
import time
import wget
from Mizuki.utils.ut import get_arg
from pyrogram import filters, types, Client
from pyrogram.types import Message

@Jebot.on_message(filters.command("saavn"))
async def song(client, message):
    message.chat.id
    user_id = message.from_user["id"]
    #args = get_arg(message) + " " + "song"
    #if args.startswith(" "):
        #await message.reply("<b>Enter a song name❗\n\nExample: `/saavn guleba`</b>")
        #return ""
    args = message.text.split(None, 1)
    args = str(args)
    args = args + " " + "song"
    m = await message.reply_text("<b>Downloading your song, Plz wait 🥺\n\nPowered by @Infinity_BOTs 🇱🇰</b>")
    try:
        r = requests.get(f"https://snobybuddymusic.herokuapp.com/result/?query={args}")
    except Exception as e:
        await m.edit(str(e))
        return
    sname = r.json()[0]['song']
    slink = r.json()[0]['media_url']
    ssingers = r.json()[0]['singers']
    file = wget.download(slink)
    ffile = file.replace("mp4", "m4a")
    os.rename(file, ffile)
    await message.reply_audio(audio=ffile, title=sname,
                              performer=ssingers)
    os.remove(ffile)
    await m.delete()
