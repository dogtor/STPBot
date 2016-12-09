#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
import logging
import json
import os
import config
import random
import requests as req
import commands
import urllib2
import urllib
import requests
import telebot
import ConfigParser
from telebot import types
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
bot = telebot.TeleBot(config.token)
#SikTirMirza
kir = "\n\n \033[01;31m Onlinam Dadach <3 \033[0m"
print(kir)
bot.send_message(config.father,"Babaee Online Shodam :|:D", parse_mode='markdown')
@bot.message_handler(commands=['start','help'])
def start(m):
 bot.send_message(m.chat.id,
 '''*Hi Welcome To Sticker To Photo Bot*

 _Commands Bot_ :
   /help
   /start

_My Action List_
 `1 - Send Me Stickerâ–¶ï¸Get It As Photo`
 `2 - Send Me Photoâ–¶ï¸Get It As Sticker`


 Developer [Amoo Ali](https://telegram.me/ShopBuy)
 Like Me [Click](https://telegram.me/ThinkTeam)
 Channel [ThinkTeam](https://telegram.me/ThinkTeam)

 _Good Luck_ð''', parse_mode='markdown')
@bot.message_handler(content_types=['sticker','photo'])
def tophoto(m):
    if message.sticker:
        cid = m.chat.id
        token = config.token
        fileid = message.sticker.file_id
        path1 = bot.get_file(fileid)
        path = path1.file_path
        link = "https://api.telegram.org/file/bot{}/{}".format(token,path)
        urllib.urlretrieve(link, "sticker.png")
        sikim = open('sticker.png', 'rb')
        bot.send_sticker(cid,sikim)
    if message.photo:
        cid = m.chat.id
        token = config.token
        fileid = message.photo[1].file_id
        path1 = bot.get_file(fileid)
        path = path1.file_path
        link = "https://api.telegram.org/file/bot{}/{}".format(token,path)
        urllib.urlretrieve(link, "stick1.png")
        alleh = open('stick1.png', 'rb')
        bot.send_photo(cid,alleh)
bot.polling(True)
#end
