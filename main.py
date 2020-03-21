from components.html.html import HTML
from components.container.container import Container
from components.navbar.navbar import Navbar
import os

html = HTML()

elementDict = {
    'container': lambda: Container(),
    'navbar': lambda: Navbar(),
}

tagsList = ['navbar', 'container', 'navbar', 'container', 'container-end', 'container-end']

def generateHTML(parent, index, tagName):
    i = index
    while i < len(tagsList):
        elementTag = tagsList[i]
        element = elementDict.get(elementTag, Container)()
        
        if elementTag == f'{tagName}-end':
            return (parent, i)

        if element.isParentLike:
            appendedElement, new_i = generateHTML(element, i+1, elementTag)
            parent.appendElement(appendedElement.template)
            i = new_i
            pass
        else:
            parent.appendElement(element.template)
            # print(parent.template)
        i = i + 1
    return (parent, i)

yee, _ = generateHTML(html, 0, 'html')
print(yee.template)
with open(os.path.join(os.getcwd(), 'dump.html'), 'w') as f:
    f.write(str(yee.template.prettify()))
