from bs4 import BeautifulSoup
import feedparser
from dateutil.parser import parse

# define class object to hold parsed data fields
class rssresult(object):
    def __init__(self, title=None, link=None,published=None,img=None,summary=None,desc=None):
        self.title = title
        self.link = link
        self.published = published
        self.img = img
        self.summary = summary
        self.desc = desc

# function that takes URLs are params, then parse and save it class of array
# Testing
def GetParseResults(urls):
   resultList = []
   for i in urls:
      print (i)
      results = feedparser.parse(i)
      for x in results.entries:
         soup = BeautifulSoup(x.summary,'html.parser')
         para_1 = soup.find('p')
         para = ""
         if para_1 is not None:
             para = para_1.get_text()
         images = soup.find('img')
         src = ""
         if images is not None :
             #para = soup.find('<p>')
             src = images['src']
         d= parse(str(x.published))
         dt = d.strftime('%Y-%m-%d %H:%S')
         #print (d)
         print(dt)
         resultList.append(rssresult(x.title,x.link,dt,src,x.summary,para))
      # Sort the result object using date
      resultList.sort(key=lambda r: r.published,reverse=True)
      #print len(resultList)


   return resultList
