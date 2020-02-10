import xmltodict
import urllib.request

url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
filepath = '../samples/map5.osm'

urllib.request.urlretrieve(url, filepath)

fin = open(filepath, 'r', encoding='utf8')
xml = fin.read()
fin.close()

dct = xmltodict.parse(xml)

def return_fuel_number(type_of_obj):
    '''Values of type_of_obj:
    node - for a point
    way - for a boundary
    '''
    fuel = 0
    if type_of_obj == 'node':
        pass
    else:
        type_of_obj = 'way'
    for node in dct['osm'][type_of_obj]:
        if 'tag' in node:
            tags = node['tag']
            if isinstance(tags, list):
                for tag in tags:
                    if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                        fuel += 1
            elif isinstance(tags, dict):
                if (tags['@v']) == 'fuel':
                    fuel += 1
    return(fuel)

boundary = return_fuel_number('way')
point = return_fuel_number('node')

print (boundary + point)