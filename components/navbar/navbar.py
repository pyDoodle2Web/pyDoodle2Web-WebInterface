from bs4 import BeautifulSoup

class Navbar:
    def __init__(self):
        self.isParentLike = False

        with open('template.html') as f:
            soup = BeautifulSoup(f, 'html.parser')
        self.template = soup
