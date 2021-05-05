import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.bmkg.go.id/gempabumi/gempabumi-terkini.bmkg")
data = web.text
bs = BeautifulSoup(data,"html.parser")
for td in bs.tbody.find_all('tr'):
    tabel = td.find_all('td')
    print('no : '+ (tabel[0].text))
    print('waktu : '+ (tabel[1].text))
    print('lintang : '+ (tabel[2].text))
    print('bujur : '+ (tabel[3].text))
    print('magnitudo : '+ (tabel[4].text))
    print('kedalaman : '+ (tabel[5].text))
    print('wilayah : '+ (tabel[6].text))
    print('\n')