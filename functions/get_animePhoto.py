import requests, json

def get_photo() :
  res = requests.get("https://api.waifu.pics/sfw/waifu")
  dat = json.loads(res.text)
  # print(dat)
  # print(dat['url'])
  return dat['url']