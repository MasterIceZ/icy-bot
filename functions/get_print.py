from replit import db

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