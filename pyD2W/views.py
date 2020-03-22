
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .ocr import OCR
from django.core.validators import validate_image_file_extension


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
            tagsList = OCR(uploaded_file.name).readText()
            
        except Exception:
            context['error'] = 'Error Occurred! Make sure the uploaded file is an Image'
        
    return render(request, 'upload.html', context)
