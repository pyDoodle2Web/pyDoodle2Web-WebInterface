from bs4 import BeautifulSoup
import os


class Navbar:
    def __init__(self, darkMode=False, navbarTitle = 'Navbar'):
        self.name = 'navbar'
        self.isParentLike = False

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'template.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
        nav = soup.find('nav')
        if darkMode:
            nav['class'] = 'navbar navbar-expand-lg navbar-dark bg-dark'
        else:
            nav['class'] = 'navbar navbar-expand-lg navbar-light bg-light'
  
        
        self.template = soup
        
        # print(f'darkMode: {darkMode}')

