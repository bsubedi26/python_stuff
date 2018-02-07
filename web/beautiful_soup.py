import requests
from bs4 import BeautifulSoup as bs

query = 'york'
# url = 'https://www.google.com/search?q=' + query
url = 'https://www.github.com/search?q=' + query

res = requests.get(url)
# raise error if response is bad
res.raise_for_status()

html = bs(res.text, 'html.parser')
titles = html.select('h3 a')
print(titles[0])

result = []
for i in range(10):
    txt = titles[i].text
    result.append(txt)

print(result)
