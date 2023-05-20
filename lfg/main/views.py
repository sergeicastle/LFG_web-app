from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request, ):
    return render(request, 'main/allideas.html', {'title': 'Главная страница'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
