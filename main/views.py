from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    data = {'title':'Главная страница' }
    return render(request, 'main/index.html', data)
def about(request):
    return render(request, 'main/about.html')
def maps(request):
    return render(request, 'main/maps.html')
