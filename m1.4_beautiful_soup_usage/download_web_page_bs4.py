from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
s = str(html)
soup = BeautifulSoup(s, "html.parser")
for a in soup.find_all('a', href=True):
    print(a['href'])