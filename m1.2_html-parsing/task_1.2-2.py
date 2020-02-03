import re
import collections

from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s = str(html)
regex = '<code>(.*?)</code>'
# Список всех совпадений
results = re.findall(regex, s)

c = collections.Counter()
for word in results:
    c[word] += 1

most_common_words = c.most_common(3)

final_res = dict(most_common_words)

print(final_res)

print("Наиболее встречающиеся строки: ")
for i in (sorted(final_res.keys())):
    print (i, end=' ')

