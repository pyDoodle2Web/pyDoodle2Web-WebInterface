from bs4 import BeautifulSoup
import os

class Footer:
    def __init__(self):
        self.name = 'footer'
        self.isParentLike = False

        with open(os.path.join(os.realpath(footer.py), 'components', 'footer', 'template.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
        self.template = soup