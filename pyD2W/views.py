
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
import json
from django.core.files.base import ContentFile


def home(request):
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
                'message':
                "Error Occurred! Make sure the uploaded file is an Image"
            }
            return HttpResponse(json.dumps(payload), status=400)

    return HttpResponse(
        json.dumps({'error': 'not a POST request'}),
        status=400)


def generate(request):
    if request.method == 'POST':
        tags = request.POST.dict().get('tags', '')
        tags = tags.strip('][').split(',')
        darkMode = request.POST.dict().get('darkMode', False)
        tagData = request.POST.dict()
        darkMode = True if darkMode == 'true' else False
        html, _ = HTMLGenerator(tags, darkMode=darkMode).generateHTML()
        html = DynamicHtmlGenerator(html.template, tagData).add_data_to_html()
        htmlString = str(html)

        payload = {'html': htmlString}
        return HttpResponse(json.dumps(payload), status=200)
    return HttpResponse(
        json.dumps({'error': 'not a POST request'}),
        status=400)


def downloadSource(request):
    fs = FileSystemStorage(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'templates'))
    response = FileResponse(fs.open('generated.html', 'rb'),
                            content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(
        'generated.html')
    return response
