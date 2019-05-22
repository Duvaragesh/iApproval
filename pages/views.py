#
# Author Duvaragesh Kannan
#
from django.shortcuts import render
from django.views.generic import TemplateView
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your views here.
def home(request):
    from pages.validator import validator
    #nameoffile = ''
    if request.method == 'POST':
        uploaded_file =request.FILES['aprvl_document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        file_path = os.path.join('media/',uploaded_file.name)
        return render(request, "home.html", {"Predicted_result":validator(request, file_path)})
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})   

def request_list(request):
        return render(request, "request_list.html", {})

def training(request):
        return render(request, "training.html", {})   
 