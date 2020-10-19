#! python
# luckygoogle.pl - script responsible for opening few searching result from Google Search

from bs4 import element
import requests, sys, webbrowser, bs4

print('Searching...')
res = requests.get('http://google.pl/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()



soup = bs4.BeautifulSoup(res.text, features="html.parser")

link_elems = soup.select('.kCrYT a')
print(link_elems[0])
print(link_elems[1])
num_open = min(5, len(link_elems))

print(num_open)


for i in range(num_open):
    webbrowser.open('http://google.pl' + link_elems[i].get('href'))