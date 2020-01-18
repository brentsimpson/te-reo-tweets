#!/usr/bin/env python3

import json
from bs4 import BeautifulSoup
import requests

english_terms = open("en.dic").read().splitlines() #opens English dictionary and reads terms into list

word_info = open('info.json') #opens the JSON file which records the number of the previous word used
current_word = json.load(word_info)
prev_word = int(current_word['word_number'])

print(prev_word) #prints the number of the word
print(english_terms[prev_word]) #Looks up word by index in list and prints

next_item = {}

prev_word = int(prev_word+1)

next_item['word_number'] = prev_word

print next_item

num_write = open('info.json', 'w')
num_write.write(json.dumps(next_item,encoding='UTF-8'))
num_write.close()

MaoriDict = 'https://maoridictionary.co.nz/search?keywords=' + english_terms[prev_word] 

print('URL string: ' + MaoriDict)

source = requests.get(MaoriDict).text  #gets the page from Maori Dictionary

soup = BeautifulSoup(source, 'lxml')

# Extracts all the H2 headings for word returned
for word in soup.find_all('h2', class_="title", limit=3):
    word = word.get_text(strip=True) 
    word = word[:-4]

    print(word)










