import requests
from lxml import html

totalnoofpages = 1617
with open("relatedtags.csv", 'a+') as file:
    header = '{},{}\n'.format("Tag", "Related Tags")
    file.write(header)

for x in range(1, totalnoofpages+1):

    relatedurl = []
    url = 'https://stackoverflow.com/tags?page='+ str(x)+'&tab=popular'
    print(url)
    data = requests.get(url)
    tree = html.fromstring(data.content)
    tags = tree.xpath('//a[@class="post-tag"]/text()')
    links = tree.xpath('//a[@class="post-tag"]/@href')

    for k in links:

        url_t = 'https://stackoverflow.com/'+ str(k)
        print(url_t)
        data_t = requests.get(url_t)
        tree = html.fromstring(data_t.content)
        relttags = tree.xpath('//div[@class="module js-gps-related-tags"]/div/a/text()')
        s = ','.join(relttags)
        d = s.replace(',', ' : ')
        relatedurl.append(d)

    with open("relatedtags.csv", 'a+') as file:

        for items in zip(tags,relatedurl):

            datawrites = '{},{}\n'.format(items[0].replace(',', ''), items[1].replace(',', ''))
            file.write(datawrites)

            print(datawrites)
