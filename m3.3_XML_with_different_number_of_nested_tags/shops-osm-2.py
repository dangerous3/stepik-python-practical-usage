import xmltodict

fin = open('../samples/map3.osm', 'r', encoding='utf-8')
text = fin.read()
fin.close()

names = []
dct = xmltodict.parse(text)

shops = 0

for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        flag = False
        name = 'noname'
        #print(tags)
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@k'] == 'shop' and tag['@v'] == 'supermarket':
                    shops += 1
                    flag = True
                if '@k' in tag and tag['@k'] == 'name':
                    name = tag['@v']
        if flag:
            names.append(name)
print(shops)
print(names)