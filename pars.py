from bs4 import BeautifulSoup
import requests
import csv


def ParseR():

    """ФУНКЦИЯ ПАРСИТ ССЫЛКИ РОССИЙСКИХ ТРЕНДОВЫХ АКЦИЙ"""

    comp = []
    url = 'https://ru.investing.com/equities/trending-stocks'
    request = requests.get(url)
    html = BeautifulSoup(request.text, "html.parser")
    tbody = html.find('tbody')
    tr = tbody.find_all('tr')
    for i in tr:
        comp.append('https://ru.investing.com' + i.find('a').get('href'))
    return comp


with open('trending-stocks.csv', 'w', newline="") as d:
    writer = csv.writer(d)
    for i in ParseR():
        writer.writerow([i])
