
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.http import HttpResponse
from django.http import FileResponse
from .ocr import OCR
from django.core.validators import validate_image_file_extension
from generator.main import HTMLGenerator
import os


def home(request):
    return render(request, 'home.html')


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        try:
            validate_image_file_extension(uploaded_file)
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)
            print(name)
            tagsList = OCR(name).readText()
            html, _ = HTMLGenerator(tagsList).generateHTML()
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates', 'generated.html'), 'w') as f:
                f.flush()
                f.write(str(html.template.prettify()))
            context['generated_url'] = True
        except Exception:
            context['error'] = 'Error Occurred! Make sure the uploaded file is an Image'

    return render(request, 'upload.html', context)


def generated(request):
    return render(request, 'generated.html')


def downloadSource(request):
    fs = FileSystemStorage(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates'))
    response = FileResponse(fs.open('generated.html', 'rb'), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('generated.html')
    return response