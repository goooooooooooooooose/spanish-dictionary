import requests
import re
from bs4 import BeautifulSoup

SPANISHDICT = 'https://www.spanishdict.com/'
WORD = 'enojado'
TRANSLATION_URL = SPANISHDICT + '/translate/' + WORD

page = requests.get(TRANSLATION_URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Hardcoded values that are subject to error.
# Will need to update the logic to be more general
definitions_class_id = 'lbHJ7w6W'
en_words_class_id = 'UlJJEaZY' 

en_definitions = soup.findAll('div', attrs={'class':definitions_class_id})
en_definition_words = []

for defn in en_definitions:
    if defn.find('div', attrs={'lang': 'en'}) is not None:
        span_text = defn.find('span', attrs={'class': en_words_class_id}).text
        defn_text = re.search('\((.*?)\)', span_text)
        en_definition_words.append(defn_text.group(1))

print('Possible translations for {WORD} include {DEFINITIONS_LIST}.'.format(WORD=WORD, DEFINITIONS_LIST=','.join(en_definition_words)))

if __name__ == '__main__':
    print('hey')
