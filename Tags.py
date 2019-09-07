import requests
from lxml import html

totalnoofpages = 1617
file = open("tags.txt", "a+")

for x in range(totalnoofpages+1):

    url = 'https://stackoverflow.com/tags?page='+ str(x)+'&tab=popular'
    print(url)

    data = requests.get(url)
    tree = html.fromstring(data.content)
    tags = tree.xpath('//a[@class="post-tag"]/text()')
    file = open("data.txt", "a+")

    for x in tags:
        file.write(x + "\n")

    print(tags)
