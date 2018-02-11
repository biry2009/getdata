import urllib.request
from bs4 import BeautifulSoup

headers = {'Accept-Language': 'en-US,en;q=0.5',
           'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

f = open("wiki.txt", "r")
fp = open("table.txt", "w")


for line in f:
    line = line.strip('\n')
    url = "https://www.godaddy.com/tlds/" + line[1:] + "-domain"
    alink = "<a href=" + str(url)  + "target=_blank >" + "Registe a" + line + "domain</a>"

    try:
        req = urllib.request.Request(url, None, headers)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, "lxml")

        if soup.find('span', {"class": "text-purchase"}) is not None:
            current_price = soup.find('span', {"class": "text-purchase"}).string

        if soup.strike is not None:
            promo_price = soup.strike.string
        else:
            promo_price = current_price

        if promo_price is not None:
            fp.write("<tr><td>" + str(line) + "</td>" + "<td>" + str(promo_price.encode('utf-8')) + "</td><td>" + str(current_price.encode('utf-8')) + "</td><td>" + alink + "</td></tr>")
    except urllib.error.URLError:
        pass
f.close()
fp.close()