from urllib.request import urlopen
from bs4 import BeautifulSoup
from random import choice
import re

times = int(input("How many times you want to repeat: "))

base_url = "https://zh.wikipedia.org"
history = ["/wiki/%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2"]
compiled_re = re.compile(r"^/wiki/(%.{2})+$")

for i in range(times):
    url = base_url + history[-1]
    html = urlopen(url).read().decode('utf-8')

    soup = BeautifulSoup(html, features='lxml')
    print(i + 1, '\t', soup.find('h1').get_text())

    sub_urls = soup.find_all("a", {"href": compiled_re})
    history.append(choice(sub_urls)['href'])
