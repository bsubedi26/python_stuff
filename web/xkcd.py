import os
import requests
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient

url = 'https://xkcd.com/'
client = MongoClient('mongodb://localhost:27017')
db = client['scraper-python']

def scrape_recursive(response):
    html = bs(response.text, 'html.parser')
    titles = html.select('#ctitle')
    title = titles[0].get_text()
    images = html.select('#comic img')
    a_tag = html.select('a[accesskey=p]')[0]
    next_link = a_tag.get('href')

    if len(images) == 0:
        # image does not exist, create default values
        image_url = 'image_url'
        image_title = 'image_title'
    else:
        image_url = images[0].get('src')
        image_title = images[0].get('title')
        comicUrl = 'https:' + image_url
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd_images', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    print(next_link)
    document = {
        'title': title,
        'image_title': image_title,
        'image_url': image_url,
        'next_link': next_link
    }
    r = db.xkcd.insert_one(document)

    # last href has #
    if next_link.find('#') == -1:
        res = requests.get(url + next_link)
        res.raise_for_status()
        return scrape_recursive(res)


def main():
    res = requests.get(url)
    # raise error if response is bad
    res.raise_for_status()
    scrape_recursive(res)


if __name__ == '__main__':
    main()
