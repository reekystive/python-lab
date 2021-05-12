from urllib.request import urlopen
from bs4 import BeautifulSoup
from random import choice
import re
import ssl

times = int(input("How many times you want to repeat: "))

base_url = "https://zh.wikipedia.org"
history = ["/zh-cn/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB"]
compiled_re = re.compile(r"^/wiki/(%.{2})+$")

ssl._create_default_https_context = ssl._create_unverified_context

for i in range(times):
    url = base_url + history[-1]
    html = urlopen(url).read().decode('utf-8')

    soup = BeautifulSoup(html, features='lxml')
    print(i + 1, '\t', soup.find('h1').get_text())

    sub_urls = soup.find_all("a", {"href": compiled_re})
    history.append(choice(sub_urls)['href'].replace('/wiki/', '/zh-cn/'))
