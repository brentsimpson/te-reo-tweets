#te-reo-tweets

Hello. This is the git page for a project that I'm very, very, slowly working on to use the Twitter platform for assistance in using Te Reo Maori in everyday contexts - in this case, mostly *on* Twitter.

Firstly, the bot will Tweet out a Maori word every day and attempt to provide a brief description in English for that term. Currently this Python program *Maori-Dictionary.py* can be run from the command line and takes a search term, in either Pakeha English or Maori, and returns the related term (without the definition) scraped from Maoridictionary.com. The tweeting of a term twice a day contains a pedagogical dimension (ako), but also aims to keep the account active in the minds of it's Followers.   

Secondly, the bot can be queried via either DM just @username), and returns a crafted DM for the term requested. This makes it possible to make these requests public rather than private, and contribute towards displaying a sort of List of recently requested terms. The aim of this functionality is unique in that it aims to provide quick access to the Maori Dictionary via a 3rd party so that users may include more Te Reo in their tweets. Switching apps to the Maori Dictionary mobile app can be time-consuming and may detract from utilizing Te Reo on Twitter. Similar functionality exists already on Twitter. 

Note: it has been difficult for me to discern the copyright implications of this project in respect to scraping information from maoridictionary.com. Copyright information on maoridictionary.com is very vague, in fact almost non-existent apart from a footer. Many of the sources provided by Maoridictionary.com are actually out of copyright themselves in New Zealand, so the issue would seem more complex and I am willing to engage in this conversation.

Next steps: 

**First Phase** 
Reading of mi_NZ.dic (list of Te Reo words) and generating request based on this.
Recording place on the list
Generating request to maoridictionary.com for term
Creating Tweet
Tweeting

**Second Phase**
Twitter API stuff
Bot interaction on Twitter








