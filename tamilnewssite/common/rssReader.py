from bs4 import BeautifulSoup
import feedparser

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
         resultList.append(rssresult(x.title,x.link,x.published,src,x.summary,para))
      #print len(resultList)


   return resultList
