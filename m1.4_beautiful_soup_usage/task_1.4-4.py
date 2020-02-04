import requests
from bs4 import BeautifulSoup

page = requests.get("https://stepik.org/media/attachments/lesson/209723/3.html")
soup = BeautifulSoup(page.content, 'html.parser')

table_numbers_cells = soup.find_all('td')
sum = 0

for i in table_numbers_cells:
    num_value = i.get_text()
    sum = sum + int(num_value)

print("Сумма равна: " + str(sum))
