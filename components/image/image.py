from bs4 import BeautifulSoup
import os
import random

class Image:
    def __init__(self):
        self.name = 'card'
        self.isParentLike = False

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'template.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
        self.template = soup
        card_image = soup.find('img') 
        card_image['src'] = f'https://picsum.photos/id/{random.randint(0, 1000)}/400/400'