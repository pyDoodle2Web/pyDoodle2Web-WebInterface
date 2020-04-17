try:
    from PIL import Image
except ImportError:
    import PIL.Image
import PIL
import pytesseract
import os
from difflib import get_close_matches

class OCR:
    def __init__(self, imageName: str):
        self.imageName = imageName
        self.real_tags = ['container', 'row', 'coloumn', 'navbar', 'image', 'card', 'container-end', 'row-end', 'coloumn-end', 'carousel', 'text', 'jumbotron']
        # self.allowed_tags = ['container', 'row', 'coloumn', 'navbar', 'image', 'card', 'column', 'cofoumm']

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
        print(tags)
        for tag in tags:
            try:
                close_match = get_close_matches(tag.lower(), self.real_tags, n = 1, cutoff = 0.6)
                if close_match[0] in self.real_tags:
                    final_tags.append(close_match[0])
            except Exception as e:
                print(e, tag)
                pass
        # print(final_tags)
        return final_tags


    def readText(self):
        try:
            path = os.path.join(os.path.abspath('./'), 'media', self.imageName)
            print(path)
            text = pytesseract.image_to_string(path)
            tags = self.builder(text)
            a= self.fixTags(tags)
            return a
        except PIL.UnidentifiedImageError:
            print('Could not read the image file, check filetype.')

        except Exception as e:
            print(e)
            

