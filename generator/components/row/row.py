from bs4 import BeautifulSoup
import os


class Row:
    def __init__(self):
        self.name = 'row'
        self.isParentLike = True

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'template.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
        self.template = soup
        self.children = []

    def appendElement(self, element):
        if self.isParentLike:
            try:
                self.template.findChild().append(element)
            except Exception as e:
                print(e)
                pass
        else:
            raise Exception('This element is not a parent like element, cannot append child')
