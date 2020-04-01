from bs4 import BeautifulSoup


class DynamicHtmlGenerator:

    def __init__(self, html,  tagData= {} ):
        self.tagData = tagData
        self.html = html

    def add_data_to_html(self):
        for tagname, tagInfo in self.tagData.items():
            if tagname == 'navbar':
                self.html.template.find(class_="navbar-brand").string = tagInfo
        print(self.html.template.find(class_="navbar-brand").string)
        return self.html


