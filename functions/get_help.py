s = list() #init list of commands

s = [
  "$help for help",
  "$source for source code",
  "$version for check last update of bot",
  "$q or $quote for Quotes",
  "$add [Quote] for add Quote",
  "$remove [Quote] for remove Quote",
  "$list for List of Quotes",
  "$fixed for Fixed Quotes",
  "$anime for anime quote",
  "$greet for Greetings",
  "$กินไรดี for asking what should you eat",
  "$newmenu for add menu",
  "$remenu [Menu] for remove menu",
  "$say to say somthing",
  "$mean [word] to search for definitions of the word",
  "$report for report bug"
]

#implement join function bc of the programmer didn't know how to use LMAO

rel = ""
for a in s :
  rel += a + '\n '

ans = '```nim\nCommand List\n ' + rel + '```' 

def get_com ():
  return ans
