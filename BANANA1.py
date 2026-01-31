import requests
from bs4 import BeautifulSoup

response = requests.get('http://127.0.0.1:5500/apropos.html')
soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')
for img in images:
    print(img['src'])
titre_h1 = soup.find_all('h1')
titre_h2 = soup.find_all('h2')
titre_h3 = soup.find_all('h3')

print("LES TITRE") 

for h1 in titre_h1:
    print(h1.text)
for h2 in titre_h2:
    print(h2.text)
for h3 in titre_h3:
    print(h3.text)

paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.text)
lien = soup.find_all('a')
for a in lien:
    print(a['href'])