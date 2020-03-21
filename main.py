from components.html.html import HTML
from components.container.container import Container
from components.navbar.navbar import Navbar
from components.card.card import Card


import os

html = HTML()

elementDict = {
    'container': lambda: Container(),
    'navbar': lambda: Navbar(),
    'card': lambda : Card(),
}

tagsList = ['navbar', 'container', 'card', 'container',  'container-end']

def generateHTML(parent,  tagName: str, index = 0,):
    i = index
    while i < len(tagsList):
        elementTag = tagsList[i]
        element = elementDict.get(elementTag, Container)()
        
        if elementTag == f'{tagName}-end':
            return (parent, i)
        if element.isParentLike:
            appendedElement, new_i = generateHTML(element, elementTag, i+1)
            parent.appendElement(appendedElement.template)
            i = new_i
            pass
        else:
            parent.appendElement(element.template)

        i = i + 1
        
    return (parent, i)

yee, _ = generateHTML(parent = html, tagName = 'html')
print(yee.template)
print(type(yee))
with open(os.path.join(os.getcwd(), 'dump.html'), 'w') as f:
    f.write(str(yee.template.prettify()))
