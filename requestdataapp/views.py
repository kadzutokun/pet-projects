from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.files.storage import FileSystemStorage
from . import forms
def process_get_view(request: HttpRequest) -> HttpResponse:
    name = request.GET.get('name','user')
    a = request.GET.get('a','')
    b = request.GET.get('b','')
    result = a + b

    context = {
        "name":name,
        "a": a,
        "b": b,
        "result": result
    }

    return render(request, 'requestdataapp/request-query-params.html', context = context)

def user_form(request:HttpRequest) -> HttpResponse:
    
    
    
    context = { 
        "form": forms.BioFrom

    }


    return render(request, 'requestdataapp/user-bio-form.html', context = context)

def handle_file_upload(request:HttpRequest) -> HttpResponse:
    if request.method == "POST" and request.FILES.get("myfile"):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        max_size = 1000000
        try:
            if request.FILES['myfile'].size > max_size:
                raise FileExistsError
        except FileExistsError:
            return print('Файл слишком большой')
        else:
            filename = fs.save(myfile.name, myfile)
            print('Файл сохранен', filename)

    return render(request, 'requestdataapp/file-upload.html')


