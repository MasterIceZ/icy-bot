import discord
import os
import random
from replit import db
from runner import alive
import requests
import json
import time

client = discord.Client()

ver = '1.0.2.0'
date2day = '08-2-2021'

def get_mean(name) :
  headers = {
    'x-rapidapi-key': "df9db79419msh0330d70ce8835cep13b3acjsn2a63a4bbcb0f",
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }
  #uu = "https://wordsapiv1.p.rapidapi.com/words/incredible/definitions"
  uu = "https://wordsapiv1.p.rapidapi.com/words/" + name + "/definitions"
  res = requests.request("GET",uu,headers=headers)
  dat = json.loads(res.text)
  print(dat['definitions'][0]['definition'])
  return dat['definitions']


def get_meme() :
  res = requests.get("https://api.imgur.com/3/g/memes/jFLlwhY")
  dat = json.loads(res.text)
  print(dat)
  return "hello"

def get_anime():
  res = requests.get("https://animechanapi.xyz/api/quotes/random")
  dat = json.loads(res.text)
  return dat['data']

def update_icy(icy_message,cha):
  if cha in db.keys():
    ice = db[cha]
    ice.append(icy_message)
    db[cha] = ice
  else :
    db[cha] = [icy_message]

def delete_icy(idx,cha):
  ice = db[cha]
  if len(ice) > idx:
    del ice[idx]
  db[cha] = ice

def gin_add(mass,cha) :
  x = cha + "hew"
  if x in db.keys() :
    a = db[x]
    a.append(mass)
    db[x] = a
  else :
    db[x] = [mass]

def gin_rem(idx,cha):
  a = cha + "hew"
  ice = db[a]
  if len(ice) > idx:
    del ice[idx]
  db[a] = ice
  

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

command_list = "```nim\nCommand List\n $help for help\n $source for source code\n $version for check last update of bot\n $q or $quote for Quotes\n $add [Quote] for add Quote \n $remove [Quote] for remove Quote\n $list for List of Quotes\n $fixed for Fixed Quotes\n $anime for anime quote\n $greet for Greetings\n $กินไรดี for asking what should you eat\n $newmenu for add menu\n $remenu [Menu] for remove menu\n $say to say somthing\n $report for report bug```"

def get_poke(s) :
  a = "https://pokeapi.co/api/v2/pokemon/" + s
  res = requests.get(a)
  dat = json.loads(res.text)
# print(dat)
  b = dat['types'][0]['type']['name']
  return b

def get_move(s) :
  a = "https://pokeapi.co/api/v2/pokemon/" + s
  res = requests.get(a)
  dat = json.loads(res.text)
  used = []
  rand1 = random.randint(0,len(dat['moves'])-1)
  used.append(rand1)
  rand2 = random.randint(0,len(dat['moves'])-1)
  for rand2 in used :
    rand2 = random.randint(0,len(dat['moves'])-1) 
  used.append(rand2)
  rand3 = random.randint(0,len(dat['moves'])-1)
  for rand3 in used :
    rand3 = random.randint(0,len(dat['moves'])-1) 
  used.append(rand3)
  rand4 = random.randint(0,len(dat['moves'])-1)
  for rand4 in used :
    rand4 = random.randint(0,len(dat['moves'])-1) 
  used.append(rand4)
  ans = []
  for x in used :
    us = dat['moves'][x]['move']['name']
    ans.append(us)
  return ans

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
  if msg.content.startswith('$say') :
    s = msg.content.split('$say ',1)[1]
    await msg.channel.send(s)
  if msg.content == '$meme' :
    q = get_meme()
    await msg.channel.send(q)
  if msg.content == '$anime':
    q = get_anime()
    ans = q[0]['quote'] + "\n -" + q[0]['character'] + " [" + q[0]['anime'] + "]"
    await msg.channel.send(ans)
  if msg.content == '$help':
    await msg.channel.send(command_list)
# options = ls
  if "icy" in db.keys():
    options = db["icy"]
  if msg.content == '$quote':
    cha = msg.guild.name
    icy = random.choice(db[cha])
    await msg.channel.send(icy)
  if msg.content == '$q':
    cha = msg.guild.name
    icy = random.choice(db[cha])
    await msg.channel.send(icy)

  if msg.content.startswith('$add'):
    icy_message = msg.content.split('$add ', 1)[1]
    cha = msg.guild.name
    update_icy(icy_message,cha)
    await msg.channel.send("Added Success!~")
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
        return 
      if idx > len(db[cha]) :
        await msg.channel.send("ไม่มีโว้ย จะส่งมาทำเหี้ยไร")
        return 
      delete_icy(idx,cha)
      icy_msg = db[cha]
      await msg.channel.send(icy_msg)
  if msg.content == '$list':
    cha = msg.guild.name
    icy = []
    if cha in db.keys():
      icy = db[cha]
    await msg.channel.send(icy)
  
  if msg.content.startswith('$fixed'):
    idx = int(msg.content.split('$fixed', 1)[1])
    cha = msg.guild.name
    if idx > len(db[cha]) :
      await msg.channel.send("ไม่มีโว้ย จะส่งมาทำเหี้ยไร")
      return
    await msg.channel.send(db[cha][idx - 1])

  if msg.content.startswith('$newmenu'):
    icy_message = msg.content.split('$newmenu ', 1)[1]
    cha = msg.guild.name
    gin_add(icy_message,cha)
    await msg.channel.send("Added Success!~")
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
        return 
      idx = ic.index(i)
      print(ic)
      if idx > len(db[cha+"hew"]) :
        await msg.channel.send("ไม่มีโว้ย จะส่งมาทำเหี้ยไร")
        return 
      gin_rem(idx,cha)
      cha += "hew"
      icy_msg = db[cha]
      await msg.channel.send(icy_msg)

  if msg.content == '$greet' :
    await msg.channel.send(random.choice(greet))
  if msg.content == "$กินไรดี" :
    await msg.channel.send(random.choice(db[msg.guild.name+"hew"]))
  if msg.content.startswith('$luv') :
    icy = msg.content.split('$luv', 1)[1]    
    ans = random.choice(lover) + icy
    await msg.channel.send(ans)
  if msg.content.startswith("$pokemon") :
    st = msg.content.split('$pokemon ',1)[1]
    poke = get_poke(st)
    move = get_move(st)
    m1 = "[ " + move[0] + " ]"
    m2 = "[ " + move[1] + " ]"
    m3 = "[ " + move[2] + " ]"
    m4 = "[ " + move[3] + " ]"
    mx = m1 + " " + m3 + "\n" + m2 + " " + m4
    ans = "```Type : " + poke + "\nMoves \n" + mx + "```" 
    await msg.channel.send(ans);
  if msg.content.startswith('$mean') :
    a = msg.content.split('$mean ',1)[1]
    dat = get_mean(a)
    l = len(dat)
    for i in range(0,l,1) :
      await msg.channel.send(str(i+1) + ". " + dat[i]['definition'])
  if any(word in msg.content for word in funny) :
    await msg.channel.send("ตลกมากมั้งไอเวร ตกนรกไป")
  if any(word in msg.content for word in banner) or msg.content == 'S A U C E':
    ans = "sauce หน้ามึงอ่ะมีแต่ source โว้ย"
    await msg.channel.send(ans)
  if msg.content == "$source" :
    await msg.channel.send('https://github.com/MasterIceZ/icy-bot')
  if msg.content == "$version" :
    ans = '```nim\nVersion : ' + ver + '\nDate : ' + date2day + '```'
    await msg.channel.send(ans)
  if msg.guild.name != '4/2 แฟมิลี่' :
    return 
  if msg.content.startswith('$role') :
    r = msg.content.split('$role ', 1)[1]
    user = msg.author
    await user.add_roles(id(r))
  
alive()
client.run(os.getenv('TOKEN'))