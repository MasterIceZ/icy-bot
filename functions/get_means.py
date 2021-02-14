import os
import requests
import json

def get_mean(name) :
  headers = {
    'x-rapidapi-key': os.getenv('TS'),
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }
  #uu = "https://wordsapiv1.p.rapidapi.com/words/incredible/definitions"
  uu = "https://wordsapiv1.p.rapidapi.com/words/" + name + "/definitions"
  res = requests.request("GET",uu,headers=headers)
  dat = json.loads(res.text)
  print(dat['definitions'][0]['definition'])
  return dat['definitions']