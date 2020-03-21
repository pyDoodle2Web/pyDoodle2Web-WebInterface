from bs4 import BeautifulSoup
import os

class Card:
    def __init__(self):
        self.isParentLike = False

        with open(os.path.join(os.getcwd(), 'components', 'card', 'template.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
        self.template = soup
