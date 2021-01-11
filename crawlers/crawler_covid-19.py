from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

wiki_url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"
html = urlopen(wiki_url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

data_str = str(soup.find('table', {"class": "wikitable plainrowheaders sortable"}))
data_list = re.split(r"</tr>", data_str)
del data_list[0]
del data_list[-1]
del data_list[-1]
del data_list[-1]

def analyse(index):
    item_1 = data_list[index]
    item_2 = re.split(r"</th>", item_1)
    item_3 = re.split(r"</td>", item_2[2])

    country = item_2[1]
    country = re.search(r'scope="row">.*?<a href=.*?">(.*)</a>', country).group(1)
    country = country.split(r"</a>")
    country = country[0]
    country = country.replace(r'<i>', '')
    country = country.replace(r'</i>', '')

    data = item_3[:3]
    data_1 = []
    for n in data:
        if "No data" in n:
            data_1.append(None)
        else:
            n = n.replace(',', '')
            data_1.append(int(re.search(r'(\d+)', n).group(1)))
    return [country, data_1]

def analyse_world():
    item_1 = data_list[0]
    item_2 = re.split(r"</th>", item_1)

    data = item_2[2:5]
    data_1 = []

    for n in data:
        if "No data" in n:
            data_1.append(None)
        else:
            n = n.replace(',', '')
            data_1.append(int(re.search(r'">(\d+)', n).group(1)))
    return data_1

data = []
data.append(["World", analyse_world()])

count = len(data_list)
for i in range(1, count):
    data.append(analyse(i))

# file = open("data.txt", mode='w', encoding='utf-8')

for country in data:
    msg = country[0] + ", "
    msg += str(country[1][0]) + ", " + str(country[1][1]) + ", " + str(country[1][2])
    print(msg)
    # file.write(msg + '\n')
