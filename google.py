"""
Author: pengxingyun
Usage: python3 google.py <keyword>
Description: 打开Google搜索前5个链接
Version: 1.0
"""
import webbrowser, sys, pyperclip, requests, bs4

print(webbrowser)
def main():
	if len(sys.argv) > 1:
		keyword = ' '.join(sys.argv[1:])
	else:
		keyword = pyperclip.paste()

	res = requests.get('https://www.google.co.jp/search?q='+ keyword)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	linkElems = soup.select('.r a')
	numOpen = min(5, len(linkElems))

	for i in range(numOpen):
		webbrowser.open('https://www.google.co.jp/' + linkElems[i].get('href'))

if __name__ == '__main__':
	main()