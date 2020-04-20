from generator.components.html.html import HTML
from generator.components.container.container import Container
from generator.components.navbar.navbar import Navbar
from generator.components.card.card import Card
from generator.components.row.row import Row
from generator.components.coloumn.coloumn import Coloumn
from generator.components.jumbotron.jumbotron import Jumbotron
from generator.components.carousel.carousel import Carousel
from generator.components.image.image import Image
from generator.components.text.text import Text
import os
from math import floor


class HTMLGenerator:
    def __init__(self, tagsList=[], darkMode=False):
        self.html = HTML(darkMode=darkMode)
        self.elementDict = {
            'container': lambda **kw: Container(**kw),
            'navbar': lambda **kw: Navbar(**kw),
            'card': lambda **kw: Card(**kw),
            'row': lambda **kw: Row(**kw),
            'coloumn': lambda **kw: Coloumn(**kw),
            'jumbotron': lambda **kw: Jumbotron(**kw),
            'carousel': lambda **kw: Carousel(**kw),
            'image': lambda **kw: Image(**kw),
            'text': lambda **kw: Text(**kw)
        }
        self.darkModeTags = ['navbar', 'card']
        self.darkMode = darkMode
    # self.tagsList = ['navbar', 'carousel',  'container', 'row', 'coloumn',
    #                  'coloumn', 'coloumn', 'card', 'image', 'card',
    #                  'coloumn-end', 'coloumn-end', 'coloumn-end',
    #                  'row-end', 'container-end', 'container', 'row',
    #                  'coloumn', 'coloumn', 'image', 'text', 'coloumn-end',
    #                  'coloumn-end', 'row-end', 'container-end']
    # self.tagsList = tagsList

    def generateHTML(self, parent=None,  tagName: str = 'html', index=0):
        parent = self.html if not parent else parent
        i = index
        while i < len(self.tagsList):
            elementTag = self.tagsList[i]
            element = self.elementDict.get(elementTag, Container)
            element = element(
                darkMode=self.darkMode
                ) if elementTag in self.darkModeTags else element()

            if elementTag == 'coloumn':
                col_count = 0
                for j in range(index, len(self.tagsList)):
                    if self.tagsList[j] == 'coloumn':
                        col_count += 1
                    if self.tagsList[j] != 'coloumn':
                        break
                for coloumnNumber in range(col_count):
                    elementTag = self.tagsList[i]
                    element = self.elementDict.get(elementTag, Container)(
                        cols=floor(12/col_count))
                    currentColChildIndex = index + col_count + coloumnNumber
                    appendedElement, new_i = self.generateHTML(
                        element, elementTag, currentColChildIndex)
                    parent.appendElement(appendedElement.template)
                i = i + new_i + 1
                continue

            if elementTag == 'coloumn-end' or elementTag == 'row-end':
                return (parent, i)

            if elementTag == f'{tagName}-end':
                return (parent, i)

            if element.isParentLike:
                appendedElement, new_i = self.generateHTML(
                    element, elementTag, i+1)
                parent.appendElement(appendedElement.template)
                i = new_i
                pass

            else:
                parent.appendElement(element.template)

            if parent.name == 'coloumn':
                return (parent, i)

            i = i + 1

        return (parent, i)


if __name__ == '__main__':
    from .ocr import OCR
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--path',
        help='Path of the image',
        required=True)

    args = parser.parse_args()
    path = args.path
    tags = OCR(path).readText()
    html, _ = HTMLGenerator(tags).generateHTML()
    with open(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'dump.html'),
            'w') as f:
        f.write(str(html.template.prettify()))
    print(html.template)


# yee, _ = HTMLGenerator().generateHTML()
# print(yee.template)
# with open(os.path.join(os.getcwd(), 'dump.html'), 'w') as f:
#     f.write(str(yee.template.prettify()))
