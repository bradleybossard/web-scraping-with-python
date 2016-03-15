# Attempt to scrape live nation page, rendered with javascript
url_base = "http://www.livenation.com/artists/"

import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup


import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from lxml import html

context = ssl._create_unverified_context()

artist_id = 44779
url = url_base + str(artist_id)

#html = urlopen (url, context=context)
#print(html.read())
#bsObj = BeautifulSoup ( html.read ())
#chat_items = bsObj.findAll("ul", {"itemprop": "events"})
#print (chat_items)

#for item in chat_items:
#  print(item)
#  print("\n")


#Take this class for granted.Just use result of rendering.
class Render(QWebPage):
  def __init__(self, url):
    self.app = QApplication(sys.argv)
    QWebPage.__init__(self)
    self.loadFinished.connect(self._loadFinished)
    self.mainFrame().load(QUrl(url))
    self.app.exec_()

  def _loadFinished(self, result):
    self.frame = self.mainFrame()
    self.app.quit()

r = Render(url)
result = r.frame.toHtml()
#This step is important.Converting QString to Ascii for lxml to process
archive_links = html.fromstring(str(result.toAscii()))
print(archive_links)
