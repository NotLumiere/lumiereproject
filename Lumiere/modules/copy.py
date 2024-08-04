# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot module containing commands for interacting with dogbin(https://del.dog)"""

import os
import re
from Lumiere import CMD_HELP
from Lumiere.lumi import ayiin_cmd, eod, eor
from Lumiere.lumi.pastebin import PasteBin

from telethon.errors.rpcerrorlist import MediaEmptyError

from . import cmd, var


try:
    import cv2
except ImportError:
    cv2 = None

try:
    from htmlwebshot import WebShot
except ImportError:
    WebShot = None

def get_chat_and_msgid(link):
    matches = re.findall("https:\\/\\/t\\.me\\/(c\\/|)(.*)\\/(.*)", link)
    if not matches:
        return None, None
    _, chat, msg_id = matches[0]
    if chat.isdigit():
        chat = int("-100" + chat)
    return chat, int(msg_id)


@ayiin_cmd(pattern="paste(?: (-d|-n|-h|-k|-s)|$)?(?: ([\\s\\S]+)|$)")
async def paste(pstl):
    """For .paste command, pastes the text directly to a pastebin."""
    service = pstl.pattern_match.group(1)
    match = pstl.pattern_match.group(2)
    reply_id = pstl.reply_to_msg_id

    if not (match or reply_id):
        return await eod(pstl, "`Elon Musk bilang saya tidak bisa menempelkan kekosongan.`")

    if match:
        message = match.strip()
    elif reply_id:
        message = await pstl.get_reply_message()
        if message.media:
            downloaded_file_name = await pstl.client.download_media(
                message,
                var.TEMP_DOWNLOAD_DIRECTORY,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = "".join(m.decode("UTF-8") for m in m_list)
            os.remove(downloaded_file_name)
        else:
            message = message.message

    xxnx = await eor(pstl, "`Menempelkan teks ...`")
    async with PasteBin(message) as client:
        if service:
            service = service.strip()
            if service not in ["-d", "-n", "-k", "-s", "-h"]:
                return await xxnx.edit("Invalid flag")
            await client(client.service_match[service])
        else:
            await client.post()

        if client:
            reply_text = f"**Ditempel dengan sukses!**\n\n[URL]({client.link})\n[View RAW]({client.raw_link})"
        else:
            reply_text = "**Gagal mencapai Layanan Pastebin**"

    await xxnx.edit(reply_text, link_preview=False)


@ayiin_cmd(pattern="[cC]opy(?: |$)(.*)")
async def get_restriced_msg(event):
    match = event.pattern_match.group(1).strip()
    if not match:
        await event.eor("`Please provide a link!`", time=5)
        return
    xx = await event.eor("Prosesing...")
    chat, msg = get_chat_and_msgid(match)
    if not (chat and msg):
        return await event.eor(
            f"`404: Not Found!`\nEg: `https://t.me/Gabutanlu/8 or `https://t.me/c/1713457115/8`"
        )
    try:
        message = await event.client.get_messages(chat, ids=msg)
    except BaseException as er:
        return await event.eor(f"**ERROR**\n`{er}`")
    try:
        await event.client.send_message(event.chat_id, message)
        await xx.try_delete()
        return
    except MediaEmptyError:
        pass
    if message.media and message.document:
        thumb = None
        if message.document.thumbs:
            thumb = await message.download_media(thumb=-1)
        media = await event.client.download_media(message.document)
        await xx.edit("`Uploading...`")
        uploaded = await event.client.send_file(
            event.chat_id, file=media, caption="**Done.**"
        )
        await xx.delete()
        if thumb:
            os.remove(thumb)


CMD_HELP.update(
    {
        "copy": f"**Plugin : **`copy`\
        \n\n  »  **Perintah :** `{cmd}copy` <link>\
        \n  »  **Kegunaan : **Untuk Mengcopy pesan/media\
        \n\n  »  **Perintah :** `{cmd}paste` <text/reply>\
        \n  »  **Kegunaan : **Untuk Menyimpan text ke ke layanan pastebin gunakan flags [`-d`, `-n`, `-h`, `-s`, `-k`]\
        \n\n  •  **NOTE :** `-d` = **Dogbin** atau `-n` = **Nekobin** atau `-h` = **Hastebin** atau `-k` = **katbin** atau `-s` = **spacebin**\
    "
    }
)
