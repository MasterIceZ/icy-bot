import requests,json,random

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