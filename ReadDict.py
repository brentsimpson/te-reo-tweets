#!/usr/bin/env python3

import json

english_terms = open("en.dic").read().splitlines() #opens English dictionary and reads terms into list

word_info = open('info.json') #opens JSON file which records the previous word used
current_word = json.load(word_info)
prev_word = int(current_word['word_number'])

print(prev_word) #prints the number of the word
print(english_terms[prev_word]) #Looks up word by index in list and prints

next_item = {}
next_item["word_number"] = {20}

print next_item


with open('info.json', 'w') as f:
    json.dumps(next_item, f)


word_info.close()
