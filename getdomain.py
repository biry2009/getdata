import urllib.request
from bs4 import BeautifulSoup

headers = {'Accept-Language': 'en-US,en;q=0.5',
           'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

f = open("test.txt", "r")
fp = open("table.txt", "w")

url = "https://icannwiki.org/.com"

req = urllib.request.Request(url, None, headers)
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, "lxml")
s = soup.find_all('tr')

fp.write(str(s))


f.close()
fp.close()