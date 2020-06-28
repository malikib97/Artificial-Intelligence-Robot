import requests
from bs4 import BeautifulSoup
print('enter the html url\n')
x=input()
r = requests.get(x)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.find('p').get_text())