from components.html.html import HTML
from components.Container.container import Container
from components.navbar.navbar import Navbar

html = HTML()

elementDict = {
    'container': lambda x: Container(),
    'navbar': lambda x: Navbar(),
}

l = ['container', 'navbar', 'container', 'container-end', 'container-end']

def generateHTML(parent, tagName, tagsList:list):
    if len(tagsList) != 0:

        if parent.isParentLike:
            for elementTag in tagsList[1:]: 
                if 'end' in elementTag.split('-'):
                    return
                element = elementDict.get(elementTag, d=Container)()
                if element.isParentLike:
                    generateHTML(element, elementTag, tagsList[1:])
                    parent.appendElement(element)
                else:
                    parent.appendElement(element)
        else:
            parent.appendElement(element)