
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.http import HttpResponse
from django.http import FileResponse
from .ocr import OCR
from django.core.validators import validate_image_file_extension
from generator.main import HTMLGenerator
import os
import base64

from django.core.files.base import ContentFile


def home(request):
    return render(request, 'home.html')


def upload(request):
    context = {}

    if request.method == 'POST':
        darkMode = True if request.POST.getlist(
            'darkMode') and request.POST.getlist('darkMode')[0] == 'true' else False
        print(darkMode)
        uploaded_file = request.FILES['document']
        if request.POST['imageURL']:
            url = request.POST['imageURL']
            format, imgstr = url.split(';base64,') 
            ext = format.split('/')[-1] 
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
            uploaded_file = data 

        try:
            validate_image_file_extension(uploaded_file)
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)

            tagsList = OCR(name).readText()
            html, _ = HTMLGenerator(tagsList, darkMode=darkMode).generateHTML()

            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates', 'generated.html'), 'w') as f:
                f.seek(0)
                f.write(str(html.template.prettify()))
                f.truncate()

            context['generated_url'] = True
            fs.delete(uploaded_file.name)
        except Exception as e:
            context['error'] = 'Error Occurred! Make sure the uploaded file is an Image'
            print(e)

    return render(request, 'upload.html', context)


def generate(request):
    return render(request, 'generated.html')


def downloadSource(request):
    fs = FileSystemStorage(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'templates'))
    response = FileResponse(fs.open('generated.html', 'rb'),
                            content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(
        'generated.html')
    return response
