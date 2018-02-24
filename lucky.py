#! python3
# lucky.py - Opens several Google search results.

import requests
import sys
import webbrowser
import bs4

term = input('entre o termo de busca: ')
res = requests.get('https://www.google.com/search?q=' + ' '.join(term))
res.raise_for_status()


print('Googling..')

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
link_elems = soup.select('.r a')

# for i in range(len(link_elems)):
#     print(link_elems[i].get('a'))

for j in range(len(link_elems)):
    print(link_elems[j].getText())

num_open = min(5, len(link_elems))

for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))
