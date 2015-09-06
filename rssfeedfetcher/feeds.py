import urllib2
from BeautifulSoup import BeautifulSoup
import feedparser

def feeddata(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	link = soup.find('link', type='application/rss+xml')
	feed = feedparser.parse( link['href'] )
	# print feed["items"]
	# print feed
	return feed["items"]


