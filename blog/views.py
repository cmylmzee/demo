from django.shortcuts import render
from .models import yazi

# Create your views here.


def index(request):
    
    return render(request, 'pages/BlogTasarımı.html')

def blog(request):
    yazilar = yazi.objects.all()
    context = {
        'yazi': yazilar
    }
    return render(request, 'pages/blog.html', context)    

def hakkımda(request):
    return render(request, 'pages/index.html') 