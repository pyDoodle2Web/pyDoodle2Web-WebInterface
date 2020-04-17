from bs4 import BeautifulSoup
import os

class HTML:
    def __init__(self, darkMode=False):
        self.name = 'html'
        self.isParentLike = True
        self.children = []
        
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'template.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
        if darkMode:
            body = soup.find('body')
            body['style'] = 'background-color:#343a40;color:white'
        else:
            body = soup.find('body')
            body['style'] = 'background-color:white;color:black'

        self.template = soup

    def appendElement(self, element):
        if self.isParentLike:
            try:
                self.template.findChild('body').append(element)
            except Exception as e:
                print(e)
                pass
        else:
            raise Exception('This element is not a parent like element, cannot append child!')