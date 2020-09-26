# Sammy Sirak
# Webscraping Harry Potter Characters

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://magical-menagerie.com/wizardry/full-character-listing/'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
character_lines = soup.find_all('p')

master_list = []

for character in character_lines:
    character_dict = {}
    
    if len(character.text.split('-')) > 1 and "Want to advertise on Magical" not in character.text:
        character_name = character.text.split('-')[0].strip()
        character_dict['name'] = ' '.join(reversed(character_name.split(', '))).replace('?', '').strip()
        character_dict['description'] = character.text.split('-')[1]
        master_list.append(character_dict)


df = pd.DataFrame(master_list)
df.to_csv('harryPotterNames.csv', index=False)