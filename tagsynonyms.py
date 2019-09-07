import requests
from lxml import html

totalnoofpages = 47

with open("tagsynonyms.csv", 'a+') as file:
    header = '{},{}\n'.format("Master", "Synonym")
    file.write(header)
for x in range(1, totalnoofpages+1):
    url = 'https://stackoverflow.com/tags/synonyms?page='+str(x)+'&tab=newest&filter=all'
    print(url)
    data = requests.get(url)
    tree = html.fromstring(data.content)
    master = tree.xpath('//*[@id="synonyms-table"]/tr/td[1]/a/text()')
    synonym = tree.xpath('//*[@id="synonyms-table"]/tr/td[2]/a/text()')
    with open("tagsynonyms.csv", 'a+') as file:

        for items in zip(master, synonym):
            datawrites = '{},{}\n'.format(items[0].replace(',', ''), items[1].replace(',', ''))
            file.write(datawrites)
            print(datawrites)