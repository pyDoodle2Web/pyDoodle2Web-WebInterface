
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.http import HttpResponse
from django.http import FileResponse
from .ocr import OCR
from django.core.validators import validate_image_file_extension
from generator.main import HTMLGenerator
from generator.dynamic_generator import DynamicHtmlGenerator
import os
import base64
import logging
from bs4 import BeautifulSoup
import json
from django.core.files.base import ContentFile


def home(request):
    return render(request, 'index.html')
def generatedSite(request):
    return render(request, 'index.html')


def readImage(request):
    if request.method == "POST":
        if 'document' in request.FILES:
            uploaded_file = request.FILES['document']

        if request.POST.dict().get('imageUrl', False):
            url = request.POST.dict().get('imageUrl', False)
            format, imgstr = url.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
            uploaded_file = data

        try:
            validate_image_file_extension(uploaded_file)
            fileName = "uploadedFile.png" if type(
                uploaded_file) == ContentFile else uploaded_file.name
            fs = FileSystemStorage()
            name = fs.save(fileName, uploaded_file)

            tagsList = OCR(name).readText()
            payload = {'tags': tagsList, 'url': fs.url(name)}
            return HttpResponse(json.dumps(payload))

        except Exception:
            payload = {
                'message': "Error Occurred! Make sure the uploaded file is an Image"}
            return HttpResponse(json.dumps(payload), status=400)

    return HttpResponse(json.dumps({'error': 'not a POST request'}), status=400)


def generate(request):
    if request.method == 'POST':
        tags = request.POST.dict().get('tags', '')
        tags = tags.strip('][').split(',')
        darkMode = request.POST.dict().get('darkMode', False)
        tagData = request.POST.dict()
        print(darkMode)

        html, _ = HTMLGenerator(tags, darkMode=True).generateHTML()
        html = DynamicHtmlGenerator(html.template, tagData).add_data_to_html()
        htmlString = str(html)

        payload = {'html': htmlString}
        return HttpResponse(json.dumps(payload), status=200)
    return HttpResponse(json.dumps({'error': 'not a POST request'}), status=400)


def upload(request):
    context = {}

    if request.method == 'POST':
        darkMode = True if request.POST.getlist(
            'darkMode') and request.POST.getlist('darkMode')[0] == 'true' else False

        uploaded_file = request.FILES['document'] if 'document' in request.FILES else False

        if request.POST.dict().get('imageUrl', False):
            url = request.POST.dict().get('imageUrl', False)
            format, imgstr = url.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

            uploaded_file = data

        tagsList = []
        try:

            if uploaded_file:
                validate_image_file_extension(uploaded_file)
                fileName = "uploadedFile.png" if type(
                    uploaded_file) == ContentFile else uploaded_file.name
                print(fileName)
                fs = FileSystemStorage()
                name = fs.save(fileName, uploaded_file)
                context['url'] = fs.url(name)

                tagsList = OCR(name).readText()
                html, _ = HTMLGenerator(
                    tagsList, darkMode=darkMode).generateHTML()

                context['navbarTitle'] = True if 'navbar' in tagsList else False
                context['carousel'] = True if 'carousel' in tagsList else False

                with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates', 'generated.html'), 'w') as f:
                    f.seek(0)
                    f.write(str(html.template.prettify()))

            if request.POST.dict().get('navbarTitle', False) or request.POST.dict().get('carousel', False):
                tagData = {}

                if len(request.POST.getlist('navbarTitle')) > 0:
                    tagData['navbar'] = request.POST.getlist('navbarTitle')[0]
                if len(request.POST.getlist('carousel')) > 0:
                    tagData['carousel'] = request.POST.getlist('carousel')[0]

                print(os.path.join(os.path.dirname(os.path.realpath(
                    __file__)), 'templates', 'generated.html'))
                with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates', 'generated.html')) as f:
                    html = BeautifulSoup(f, 'html.parser')
                html = DynamicHtmlGenerator(html, tagData).add_data_to_html()

                with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates', 'generated.html'), 'w') as f:
                    f.seek(0)
                    f.write(str(html.prettify()))

            context['generated_url'] = True
            if uploaded_file:
                fs.delete(uploaded_file.name)
        except Exception as e:
            context['error'] = 'Error Occurred! Make sure the uploaded file is an Image' if uploaded_file else 'No file choosen!' if not context['navbarTitle'] else ''
            print(e)
            # logging.getLogger(__name__).exception()

    # return render(request, 'upload.html', context)
    return render(request, 'index.html')

# def generate(request):
#     return render(request, 'generated.html')


def downloadSource(request):
    fs = FileSystemStorage(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'templates'))
    response = FileResponse(fs.open('generated.html', 'rb'),
                            content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(
        'generated.html')
    return response
