import urllib2 
from bs4 import BeautifulSoup
import json

f = urllib2.urlopen('http://www.espn.com/nfl/statistics/team/_/stat/total')
html = f.read()
if html:
	data = []
	soup = BeautifulSoup(html, "html5lib")
	table = soup.find('table', attrs={'class':'tablehead'})
	table_body = table.find('tbody')

	rows = table_body.find_all('tr')
	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		data.append([ele for ele in cols if ele])
		
for info in data:
	for item in info:
		print item.encode("utf-8")

		
