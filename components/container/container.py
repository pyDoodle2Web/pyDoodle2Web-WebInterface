from bs4 import BeautifulSoup
import os

class Container:
    def __init__(self):
        self.name = 'container'
        self.isParentLike = True
        self.children = []

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'template.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
        self.template = soup

    def appendElement(self, element):
        if self.isParentLike:
            try:
                self.template.findChild().append(element)
            except Exception as e:
                print(e)
                pass
        else:
            raise Exception('This element is not a parent like element, cannot append child')