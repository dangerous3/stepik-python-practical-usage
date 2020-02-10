import xmltodict
import urllib.request

url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
filepath = '../samples/map4.osm'

urllib.request.urlretrieve(url, filepath)

fin = open(filepath, 'r', encoding='utf8')
xml = fin.read()
fin.close()

dct = xmltodict.parse(xml)

fuel = 0

for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                    print(tags)
                    fuel += 1
        elif isinstance(tags, dict):
            print(tags)
            if (tags['@v']) == 'fuel':
                fuel += 1

print(fuel)