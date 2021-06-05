import requests, json
from random import randint

def get_photo() :
  ls = [
    "waifu",
    "neko",
    "shinobu",
    "megumin",
    "bully",
    "cuddle",
    "cry",
    "hug",
    "awoo",
    "kiss",
    "lick",
    "pat",
    "smug",
    "bonk",
    "yeet",
    "blush",
    "smile",
    "wave",
    "highfive",
    "handhold",
    "nom",
    "bite",
    "glomp",
    "slap",
    "kill",
    "happy",
    "wink",
    "poke",
    "dance",
    "cringe"
  ]
  cat = ls[randint(0, len(ls))]
  ur = "https://api.waifu.pics/sfw/" + cat
  res = requests.get(ur)
  dat = json.loads(res.text)
  return dat['url']