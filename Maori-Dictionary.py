from bs4 import BeautifulSoup
import requests


text = raw_input("Lookup word: ")

MaoriDict = 'https://maoridictionary.co.nz/search?keywords=' + text

print('URL string: ' + MaoriDict)

source = requests.get(MaoriDict).text  #gets the page from Maori Dictionary

soup = BeautifulSoup(source, 'lxml')

# Extracts all the H2 headings for word returned
for word in soup.find_all('h2', class_="title", limit=3):
    word = word.get_text(strip=True) 
    word = word[:-4]

    print(word)

