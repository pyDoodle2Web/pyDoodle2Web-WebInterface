from bs4 import BeautifulSoup

class HTML:
    def __init__(self):
        self.isParentLike = True
        self.children = []
        
        with open('template.html') as f:
            soup = BeautifulSoup(f, 'html.parser')
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