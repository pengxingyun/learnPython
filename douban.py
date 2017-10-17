"""
Author: pengxingyun
Usage: python3 douban.py <keyword>
Description: 爬取豆瓣电影页面排名第一电影的前50条评论
Version: 1.0
"""
from urllib import request
from bs4 import BeautifulSoup as bs
import os

# 获取网页数据
def get_web_page_data(url, charset='utf-8', parser='html.parser'):
	resp = request.urlopen(url)
	html_data = resp.read().decode(charset)
	return bs(html_data, parser)


# 打开豆瓣电影首页
soup = get_web_page_data('https://movie.douban.com/cinema/nowplaying')

nowplaying_movie = soup.find_all('div', id='nowplaying')

nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')

# 获取豆瓣电影排行全部影片 1.id 2.title 3.name
nowplaying_list = []
for item in nowplaying_movie_list:
	nowplaying_dict = {}
	nowplaying_dict["id"] = item["data-subject"]
	nowplaying_dict["title"] = item["data-title"]
	for tag_img_item in item.find_all('img'):
		nowplaying_dict["name"] = tag_img_item["alt"]
		nowplaying_list.append(nowplaying_dict)

# # 把列表写入文件
with open('movie_list.json', 'w') as f:
	# for x in nowplaying_list:
	f.write(str(nowplaying_list)) # 强转为string类型

# https://movie.douban.com/subject/27038183/comments?start=20&limit=20 羞羞的铁拳影评地址 start为offset limit为数量

start = 0
limit = 50

# 格式化字符串拼接
requrl = 'https://movie.douban.com/subject/%s/comments?start=%s&limit=%s' % (nowplaying_list[0]['id'], start, limit)

soup = get_web_page_data(requrl)

comment_div_lists = soup.find_all('div', class_='comment')
# resp = request.urlopen(requrl)

eachCommentList = []
for item in comment_div_lists:
	if item.find_all('p')[0].string is not None:
		eachCommentList.append(item.find_all('p')[0].string)

print(eachCommentList)

comments = ''
for k in range(len(eachCommentList)):
	comments = comments + (str(eachCommentList[k])).strip()

with open('test.txt', 'w') as f:
	# for x in nowplaying_list:
	f.write(str(comments)) # 强转为string类型



# print(len(nowplaying_movie))
# for x in nowplaying_movie_list:
# 	print('------', x, '\n')

# print(nowplaying_movie)
# dirPath = os.path.join(os.getcwd(), 'index.html')
