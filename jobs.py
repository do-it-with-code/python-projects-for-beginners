import requests
from bs4 import BeautifulSoup
import time
import csv

r = requests.get("https://sfbay.craigslist.org/d/web-html-info-design/search/web")
soup = BeautifulSoup( r.text, "html.parser")

#print( soup )

links = soup.findAll("a", { "class":"hdrlnk" })
#print( links )

f = open('jobs.csv', 'w', newline='')
csv = csv.writer(f)

for link in links:
    #print( link.text )
    content = requests.get( link['href'] )
    time.sleep( 5 )
    desc = BeautifulSoup( content.text, "html.parser" )
    details = desc.find("p", { "class":"attrgroup"})
    more = details.findAll('span')
    compensation = more[0].text
    type = more[1].text

    title = link.text
    url = link['href']
    result = [ title, url, compensation, type ]
    print( result )

    csv.writerow( result )

f.close()
