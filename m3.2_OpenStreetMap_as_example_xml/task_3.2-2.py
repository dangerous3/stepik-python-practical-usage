import xmltodict
import urllib.request

url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'
filepath = '../samples/map2.osm'

urllib.request.urlretrieve(url, filepath)

fin = open(filepath, 'r', encoding='utf8')
xml = fin.read()
fin.close()

dct = xmltodict.parse(xml)

# Счетчик вложенных тэгов и тэгов, не имеющих потомков
counter_nested = 0
counter_not_nested = 0

for node in dct['osm']['node']:
    if 'tag' in node:
        counter_nested += 1
    else:
        counter_not_nested += 1

print('%s %s' % (counter_nested, counter_not_nested))