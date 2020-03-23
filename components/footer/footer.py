from bs4 import BeautifulSoup
import os

class Footer:
    def __init__(self):
        self.name = 'Footer'
        self.isParentLike = False

        with open(os.path.join(os.getcwd(), 'components', 'footer', 'template.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
        self.template = soup