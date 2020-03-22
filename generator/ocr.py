try:
    from PIL import Image
except ImportError:
    import PIL.Image
import PIL
import pytesseract
import os
from difflib import get_close_matches

class OCR:
    def __init__(self, imagePath: str):
        self.imagePath = imagePath
        self.real_tags = ['container', 'row', 'coloumn', 'navbar', 'col', 'image', 'card', 'container-end', 'row-end', 'coloumn-end']
        self.allowed_tags = ['container', 'row', 'coloumn', 'navbar', 'image', 'card', 'column', 'cofoumm']

    def formater(self, line: str):
        if line not in ['', ' ']:
            return line


    def builder(self, text: str):
        main_list = []
        for line in filter(self.formater, text.splitlines()):
            for i in line.strip().split():
                main_list.append(i)
        return main_list


    def fixTags(self, tags):
        final_tags = []
        for tag in tags:
            close_match = get_close_matches(tag, self.real_tags, n = 1, cutoff = 0.6)
            if close_match[0] in self.real_tags:
                final_tags.append(close_match[0])
        return final_tags


    def readText(self):
        try:
            path = os.path.join(os.getcwd(), self.imagePath)
            text = pytesseract.image_to_string(path)
            tags = self.builder(text)
            return self.fixTags(tags)

        except PIL.UnidentifiedImageError:
            print('Could not read the image file, check filetype.')

        except Exception as e:
            print(e)
            

