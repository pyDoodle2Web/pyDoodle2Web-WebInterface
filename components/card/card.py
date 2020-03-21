from bs4 import BeautifulSoup
import os
import random

class Card:
    def __init__(self):
        self.name = 'card'
        self.isParentLike = False

        with open(os.path.join(os.getcwd(), 'components', 'card', 'template.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
        self.template = soup
        card_image = soup.find('img') 
        card_image['src'] = f'https://picsum.photos/{random.randint(300, 400)}?random=1'