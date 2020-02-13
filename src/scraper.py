from bs4 import BeautifulSoup
import urllib.request

video_url = "https://www.capitalfactory.com/portfolio/"
page = urllib.request.urlopen(video_url)
soup = BeautifulSoup(page, 'html.parser')
print(soup)
