#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

r = requests.get("http://ddg.gg")
print(r.text)

'''
import logging
from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

app = Client("my_account", api_id = 1468033, api_hash = "9bd06a9bd53cee5ace0b84d25ed582ad")

hello_text = """
Вітаю новоприбулих! 
Рекомендую подивитись закріплені повідомлення та полистати пости вгору. 
Ця група містить матеріали вступу ще з 2020-го року - тобто три вступні 
кампанії: 2020, 2021, 2022 років. Тому можна почитати багато матеріалів 
про навчання на 121 спеціальності, про прохідний бад на контракт і бюджет,  
про комп техніку та аудиторії, про гуртожиток, про різні event-и та почерпнути 
багато іншої корисної для вступника інформації
"""

@app.on_message(filters.chat("@pzvntu2020") & filters.new_chat_members)
def welcome(app, message):
    try:
        app.send_message(chat_id=message.chat.id, text=hello_text)
    except PeerIdInvalid:
        pass

app.run()
'''
