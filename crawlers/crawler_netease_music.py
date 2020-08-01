from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

base_url = "https://music.163.com"
playlist_id = input("Input a Netease Music playlist ID: ")
url = base_url + "/playlist?id=" + playlist_id

html = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html, features='lxml')

playlist_name = soup.find('h2').get_text()
print("Playlist name:", playlist_name)
songs_str = str(soup.find('ul'))

songs_list = re.split(r"<li>", songs_str)
del songs_list[0]

song_names = []
song_ids = []
for s in songs_list:
    tmp = re.search(r'(\d+)">(.*)</a>', s)
    song_names.append(tmp.group(2))
    song_ids.append(tmp.group(1))

for i in range(len(song_names)):
    print(i + 1, "\tID:", song_ids[i], "\tName:", song_names[i])
