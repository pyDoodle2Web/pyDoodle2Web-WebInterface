from bs4 import BeautifulSoup
import random

class DynamicHtmlGenerator:

    def __init__(self, html,  tagData={}):
        self.tagData = tagData
        self.html = html

    def add_data_to_html(self):
        for tagname, tagInfo in self.tagData.items():
            if tagname == 'navbar':
                self.html.find(class_="navbar-brand").string = tagInfo
            if tagname == 'carousel':
                indicator = self.html.find(class_="carousel-indicators")
                carousel = self.html.find(class_="carousel-inner")
                indicator.clear()
                carousel.clear()
                print(carousel)
                for i in range(int(tagInfo)):
                    indicator.append(BeautifulSoup(
                        f'<li data-target="#carouselExampleIndicators" data-slide-to="{i}"></li>', 'html.parser'))
                    carousel.append(BeautifulSoup(
                        f'<div class="carousel-item {"active" if i == 0 else ""}"> <img class="d-block w-100" src="" alt="slide"><div class="carousel-caption d-none d-md-block"><h1>Slide {i}</h1><p>some sub heading</p> </div> </div>', 'html.parser'))
                images = carousel.findAll('img')
                for image in images:
                    image['src'] = f'https://picsum.photos/id/{random.randint(0, 1000)}/1024/500'   

        return self.html
