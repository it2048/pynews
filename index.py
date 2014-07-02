__author__ = 'xiongfanglei'
import requests
import bs4
response = requests.get('http://it2048.cn/')
soup = bs4.BeautifulSoup(response.text)
links = soup.select()


print(response.text)