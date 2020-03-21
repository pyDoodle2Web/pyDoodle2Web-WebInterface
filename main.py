from components.html.html import HTML
from components.container.container import Container
from components.navbar.navbar import Navbar
from components.card.card import Card
from components.row.row import Row
from components.coloumn.coloumn import Coloumn
import os

html = HTML()

elementDict = {
    'container': lambda: Container(),
    'navbar': lambda: Navbar(),
    'card': lambda: Card(),
    'row': lambda: Row(),
    'coloumn': lambda: Coloumn()
}

tagsList = ['navbar', 'container', 'row', 'coloumn', 'coloumn', 'coloumn',
            'card', 'card', 'card', 'coloumn-end', 'coloumn-end', 'coloumn-end', 'row-end', 'container-end']


def generateHTML(parent,  tagName: str, index=0,):
    i = index
    while i < len(tagsList):
        elementTag = tagsList[i]
        element = elementDict.get(elementTag, Container)()

        if elementTag == 'coloumn':
            col_count = 0
            for j in range(index, len(tagsList)):
                if tagsList[j] == 'coloumn':
                    col_count += 1
                if tagsList[j] == 'coloumn-end':
                    break
            for coloumnNumber in range(col_count):
                elementTag = tagsList[i]
                element = elementDict.get(elementTag, Container)()
                currentColChildIndex = index + col_count + coloumnNumber
                print(currentColChildIndex, element.template)
                appendedElement, _ = generateHTML(element, elementTag, currentColChildIndex)
                parent.appendElement(appendedElement.template)
            i = i + col_count*2
        if elementTag == 'coloumn-end':
            pass

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


yee, _ = generateHTML(parent=html, tagName='html')
# print(yee.template)
# print(type(yee))
with open(os.path.join(os.getcwd(), 'dump.html'), 'w') as f:
    f.write(str(yee.template.prettify()))
