import xmltodict
import urllib.request

url = 'https://stepik.org/media/attachments/lesson/245571/map1.osm'
filepath = '../samples/map1.osm'

urllib.request.urlretrieve(url, filepath)

fin = open(filepath, 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])