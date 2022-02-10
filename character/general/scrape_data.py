import json, requests
from xml.dom.minidom import Element
from time import sleep
from bs4 import BeautifulSoup

wiki_domain = 'https://genshin-impact.fandom.com/wiki'

key_list = []
with open('keys.json', 'r') as file:
    key_list = json.loads(file.read())

name_list = []
with open('names.json', 'r') as file:
    name_list = json.loads(file.read())

def scrape_character_element(key):
    print(f'{key[:10]:>10}', end='\r')
    name = '_'.join([ name.capitalize() for name in key.split('_') ])
    response = requests.get(f'{wiki_domain}/{name}')
    content = BeautifulSoup(response.content, features='lxml')
    element = content.find('td', attrs={ 'data-source': 'element' }).find('a').attrs['title']
    weapon = content.find('td', attrs={ 'data-source': 'weapon' }).find('a').attrs['title']
    return find

element_pair = { key:scrape_character(key) for key in key_list  }

sleep(1)
