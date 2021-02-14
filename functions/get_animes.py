import json, requests

def get_anime():
  res = requests.get("https://animechanapi.xyz/api/quotes/random")
  dat = json.loads(res.text)
  return dat['data']