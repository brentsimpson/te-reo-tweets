#!/usr/bin/env python3

import json

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
