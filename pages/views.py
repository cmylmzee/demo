from django.shortcuts import render
from django.http import HttpResponse
from blog.models import yazi


# Create your views here.


def index(request):
    yazilar = yazi.objects.all()
    context = {
        'yazi': yazilar
    }
    return render(request, 'pages/BlogTasarımı.html', context)

def about(request):
    return render(request, 'pages/about.html')    

def hakkımda(request):
    return render(request, 'pages/index.html') 