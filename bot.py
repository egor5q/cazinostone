# -*- coding: utf-8 -*-
import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


client=MongoClient(os.environ['database'])
db=client.cazinostone
users=db.users

games={}

effects=['silence','buff']
types=['deathrattle','battlecry','special']


@bot.message_handler(commands=['cazino'])
def cazino(m):
    games.update(creategame(m.chat.id))
    




def createeffect(x):
    targets=['enemy','ally']
    silence={
        'name':'silence',
        'target':random.choice(targets)
    }
    buff={
        'name':'buff',
        'target':'ally'
    }
    if x=='silence':
        return silence
    elif x=='buff':
        return buff

    
def createcard(x):
    return {
        'type':x,
        'battlecries':[],
        'deathrattles':[]
    }

def creategame(id):
    return {
        'players':[],
        'turn':1
    }
    
    

if True:
   print('7777')
   bot.polling(none_stop=True,timeout=600)

