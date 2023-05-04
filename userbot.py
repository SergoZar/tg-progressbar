#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

app = Client("my_account", api_id = 1, api_hash = "")

@app.on_message(filters.chat("@me"))
def welcome(app, message):
    try:
        app.send_message(chat_id=message.chat.id, text=message.text)
    except PeerIdInvalid:
        pass

app.run()

