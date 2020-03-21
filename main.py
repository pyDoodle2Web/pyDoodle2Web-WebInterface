from components.html.html import HTML
from components.container.container import Container
from components.navbar.navbar import Navbar
from components.card.card import Card
from components.row.row import Row
from components.coloumn.coloumn import Coloumn
import os
from math import floor

html = HTML()

elementDict = {
    'container': lambda **kw: Container(**kw),
    'navbar': lambda **kw: Navbar(**kw),
    'card': lambda **kw: Card(**kw),
    'row': lambda **kw: Row(**kw),
    'coloumn': lambda **kw: Coloumn(**kw)
}
# 'row', 'coloumn', 'navbar', 'coloumn-end', 'row-end',
tagsList = ['navbar', 'container', 'row', 'coloumn', 'coloumn', 'coloumn','coloumn',
            'card', 'card',  'card', 'row', 'coloumn', 'container', 'card','container-end','coloumn-end', 'row-end','coloumn-end' 'coloumn-end', 'coloumn-end', 'coloumn-end', 'row-end', 'container-end']


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
                if tagsList[j] != 'coloumn':
                    break
            for coloumnNumber in range(col_count):
                elementTag = tagsList[i]
                element = elementDict.get(elementTag, Container)(cols = floor(12/col_count))
                currentColChildIndex = index + col_count + coloumnNumber 
                appendedElement, new_i = generateHTML(element, elementTag, currentColChildIndex)
                parent.appendElement(appendedElement.template)
            i = i + new_i + 1
            continue

        if elementTag == 'coloumn-end' or elementTag == 'row-end':
            return (parent, i)

        if elementTag == f'{tagName}-end':
            return (parent, i)
        if element.isParentLike:
            appendedElement, new_i = generateHTML(element, elementTag, i+1)
            parent.appendElement(appendedElement.template)
            i = new_i
            continue
        else:
            parent.appendElement(element.template)

        if parent.name == 'coloumn':
            return (parent, i)

        i = i + 1

    return (parent, i)


yee, _ = generateHTML(parent=html, tagName='html')
# print(yee.template)
# print(type(yee))
with open(os.path.join(os.getcwd(), 'dump.html'), 'w') as f:
    f.write(str(yee.template.prettify()))
