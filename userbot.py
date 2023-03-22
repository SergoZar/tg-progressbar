#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

app = Client("my_account", api_id = 1468033, api_hash = "9bd06a9bd53cee5ace0b84d25ed582ad")

@app.on_message(filters.chat("@me"))
def welcome(app, message):
    try:
        app.send_message(chat_id=message.chat.id, text=message.text)
    except PeerIdInvalid:
        pass

app.run()

