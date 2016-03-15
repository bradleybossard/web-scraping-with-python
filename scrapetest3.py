# Attempt to scrape hypriot gitter archives

## url format - https://gitter.im/hypriot/talk/archives/2016/05/18
# url = "https://gitter.im/hypriot/talk/archives/2016/05/18"
url = "https://gitter.im/hypriot/talk/archives/2015/07/01"

#url =  "http://www.pythonscraping.com/pages/page1.html"

import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
#html = urlopen ( "http://www.pythonscraping.com/pages/page1.html" )
context = ssl._create_unverified_context()
html = urlopen (url, context=context)
bsObj = BeautifulSoup ( html.read ())
chat_items = bsObj.findAll("div", {"class": "chat-item"})
#print ( bsObj.h1 )
#print (bsObj)
print (chat_items)
for item in chat_items:
  print(item)
  print("\n")
