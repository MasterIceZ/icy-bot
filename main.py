import discord
import os
import random
import asyncio
from replit import db
from runner import alive
from functions.get_means import get_mean
from functions.get_animes import get_anime
from functions.get_print import update_icy, delete_icy
from functions.get_food import gin_add, gin_rem
from functions.get_help import get_com
from functions.get_animePhoto import get_photo, nsfw_photo

client = discord.Client()

ver = '1.0.2.1a'
date2day = '14-2-2021'

async def waiter() :
   await asyncio.sleep(2)

lover = [
  "รักนะคะ",
  "ทำไมน่ารักจังเลย :heart:",
  ":heart:",
  ":heart_eyes:"
]

greet = [
  "ซาหวาดดีค้าบบบ",
  "จ๊ะเอ๋ตัวเอง",
  "ดีจ้าา"
]

banner = [
  "SAUCE",
  "Sauce",
  "sauce"
]

@client.event 
async def on_ready():
  print('Icy : {0.user}666-'.format(client))
  await client.change_presence(activity = discord.Streaming(name = 'Free Fire', url = 'https://www.twitch.tv/directory/game/Garena%20Free%20Fire'))

funny = [
  "55",
  "HaHa",
  "haha",
  "Lmao",
  "lmao",
  "LMAO",
  "ฮ่า",
  "ขำ"
]

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return
  if msg.content == "$report" :
    await msg.channel.send('Please add issue at https://github.com/MasterIceZ/icy-bot/issues')
    waiter()
  if msg.content.startswith('$say') :
    s = msg.content.split('$say ',1)[1]
    await msg.channel.send(s)
    waiter()
  if msg.content == '$anime':
    q = get_anime()
    ans = q[0]['quote'] + "\n -" + q[0]['character'] + " [" + q[0]['anime'] + "]"
    await msg.channel.send(ans)
    waiter()
  if msg.content == '$help':
    await msg.channel.send(get_com())
    waiter()
# options = ls
  if msg.content == '$quote':
    cha = msg.guild.name
    icy = random.choice(db[cha])
    await msg.channel.send(icy)
    waiter()
  if msg.content == '$q':
    cha = msg.guild.name
    icy = random.choice(db[cha])
    await msg.channel.send(icy)
    waiter()

  if msg.content.startswith('$add'):
    icy_message = msg.content.split('$add ', 1)[1]
    cha = msg.guild.name
    update_icy(icy_message,cha)
    await msg.channel.send("Added Success!~")
    waiter()
  if msg.content.startswith('$remove'):
    icy_msg = []
    cha = msg.guild.name
    if cha in db.keys():
      i = msg.content.split('$remove ', 1)[1]
      ic = db[cha]
      idx = ic.index(i)
      mark = False
      for x in ic :
        if x == i :
          mark = True
          break
      if not mark : 
        await msg.channel.send("ไม่มีโว้ย จะส่งมาทำเหี้ยไร")
        waiter()
        return 
      if idx > len(db[cha]) :
        await msg.channel.send("ไม่มีโว้ย จะส่งมาทำเหี้ยไร")
        waiter()
        return 
      delete_icy(idx,cha)
      icy_msg = db[cha]
      await msg.channel.send(icy_msg)
      waiter()
  if msg.content == '$list':
    cha = msg.guild.name
    icy = []
    if cha in db.keys():
      icy = db[cha]
    await msg.channel.send(icy)
    waiter()
  
  if msg.content.startswith('$fixed'):
    idx = int(msg.content.split('$fixed', 1)[1])
    cha = msg.guild.name
    if idx > len(db[cha]) :
      await msg.channel.send("ไม่มีโว้ย จะส่งมาทำเหี้ยไร")
      return
    await msg.channel.send(db[cha][idx - 1])
    waiter()

  if msg.content.startswith('$newmenu'):
    icy_message = msg.content.split('$newmenu ', 1)[1]
    cha = msg.guild.name
    gin_add(icy_message,cha)
    await msg.channel.send("Added Success!~")
    waiter()
  if msg.content.startswith('$remenu'):
    icy_msg = []
    cha = msg.guild.name
    if cha+"hew" in db.keys():
      ic = db[cha+"hew"]
      i = msg.content.split('$remenu ', 1)[1] 
#     print(ic)
      mark = False
      for x in range(0,len(ic)) :
        if ic[x] == i :
          mark = True
          break 
      if not mark :
        await msg.channel.send("ไม่มีโว้ย จะส่งมาทำเหี้ยไร")
        waiter()
        return 
      idx = ic.index(i)
      print(ic)
      if idx > len(db[cha+"hew"]) :
        await msg.channel.send("ไม่มีโว้ย จะส่งมาทำเหี้ยไร")
        waiter()
        return 
      gin_rem(idx,cha)
      cha += "hew"
      icy_msg = db[cha]
      await msg.channel.send(icy_msg)
      waiter()

  if msg.content == '$greet' :
    await msg.channel.send(random.choice(greet))
    waiter()
  if msg.content == "$กินไรดี" :
    await msg.channel.send(random.choice(db[msg.guild.name+"hew"]))
  if msg.content.startswith('$luv') :
    icy = msg.content.split('$luv', 1)[1]    
    print(msg.content)
    ans = random.choice(lover) + icy
    await msg.channel.send(ans)
    waiter()
  if msg.content.startswith('$mean') :
    a = msg.content.split('$mean ',1)[1]
    dat = get_mean(a)
    l = len(dat)
    for i in range(0,l,1) :
      await msg.channel.send(str(i+1) + ". " + dat[i]['definition'])
      waiter()
  if any(word in msg.content for word in funny) :
    
    FUN = [
      'ตลกมากมั้งไอเวร ตกนรกไป',
      'ไม่ตลกครับ',
    ]
    
    await msg.channel.send(random.choice(FUN))
    waiter()
  if any(word in msg.content for word in banner) or msg.content == 'S A U C E':
    ans = "sauce หน้ามึงอ่ะมีแต่ source โว้ย"
    await msg.channel.send(ans)
    waiter()
  if msg.content == "$source" :
    await msg.channel.send('https://github.com/MasterIceZ/icy-bot')
  if msg.content == "$version" :
    ans = '```nim\nVersion : ' + ver + '\nDate : ' + date2day + '```'
    await msg.channel.send(ans)
    waiter()
  if msg.content == '$photo' :
    ur = get_photo()
    await msg.channel.send(ur)
    waiter()
  if msg.content == '$n_s_f_w_photo' :
    ur = nsfw_photo()
    await msg.channel.send(ur)
    waiter()
alive()
client.run(os.getenv('TOKEN'))