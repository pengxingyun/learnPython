import urllib.request
from bs4 import BeautifulSoup
import os

url = 'http://www.yidianzixun.com/article/0HMo1GMI'
res = urllib.request.urlopen(url)
html = res.read().decode('utf-8')

print(html)

# soup = BeautifulSoup(html, 'html.parser')
# result = soup.find_all('img', limit=10)
# links = []
# for content in result:
# 	links.append(content.get('src'))

# if not os.path.exists('photo'):
# 	os.makedirs('photo')

# i = 0
# for link in links:
# 	i += 1
# 	filename = 'photo/' + 'photo' + str(i) + '.gif'
# 	with open(filename, 'w') as file:
# 		urllib.request.urlretrieve(link, filename)