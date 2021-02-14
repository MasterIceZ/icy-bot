from replit import db

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