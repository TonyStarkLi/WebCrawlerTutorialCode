import requests
from bs4 import BeautifulSoup

url = 'https://tonystarkli.github.io'
data = requests.get(url=url).text
soup = BeautifulSoup(data, 'html.parser')

try:
	AllArticleSection = soup.find('section', {'id':'main'}).find_all('div', {'class':'article-inner'})
	for each in AllArticleSection:
		link = each.find('img').get('src')
		print(link)
except:
	print('error')