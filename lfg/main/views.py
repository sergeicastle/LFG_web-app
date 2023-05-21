from django.http import HttpResponseNotFound
from django.shortcuts import render


def allideas(request, ):
    return render(request, 'main/allideas.html', {'title': 'Главная страница'})


def createidea(request, ):
    return render(request, 'main/createidea.html', {'title': 'Главная страница'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
