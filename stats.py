import urllib2 

from HTMLParser import HTMLParser  

class MyHTMLParser(HTMLParser):

  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0 
    self.data = []
  def handle_starttag(self, tag, attrs):
    if tag == 'tbody':
      for name, value in attrs:
        if name == 'id' and value == 'yui_3_18_1_4_1478834569561_116':
          print name, value
          print "Encountered the beginning of a %s tag" % tag 
          self.recording = 1 


  def handle_endtag(self, tag):
    if tag == 'tbody':
      self.recording -=1 
      print "Encountered the end of a %s tag" % tag 

  def handle_data(self, data):
    if self.recording:
      self.data.append(data)

p = MyHTMLParser()
f = urllib2.urlopen('https://sports.yahoo.com/nfl/stats/byteam?group=Offense&cat=Total')
html = f.read()
p.feed(html)
print p.data
p.close()