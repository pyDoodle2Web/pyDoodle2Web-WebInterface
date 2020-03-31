from bs4 import BeautifulSoup
import os
import random

class Card:
    def __init__(self, darkMode=False):
        self.name = 'card'
        self.isParentLike = False

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'template.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
        self.template = soup
        card_image = soup.find('img') 
        card_image['src'] = f'https://picsum.photos/id/{random.randint(0, 1000)}/400/400'
        if darkMode:
            div = soup.find('div')
            div['style'] += ';background-color:#343a40;color:white;border:white solid 1px'
        else:
            div = soup.find('div')
            div['style'] += ';background-color:white;color:black'
