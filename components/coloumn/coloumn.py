from bs4 import BeautifulSoup
import os


class coloumn:
    def __init__(self):
        self.isParentLike = True

        with open(os.path.join(os.getcwd(), 'components', 'coloumn', 'template.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
        self.template = soup
        self.children = []