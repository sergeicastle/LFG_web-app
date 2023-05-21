from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Ideas
from .forms import IdeasForm


def allideas(request):
    ideas = Ideas.objects.all().order_by('-id')
    return render(request, 'main/allideas.html', {'ideas': ideas})


def createidea(request):
    error = ''
    if request.method == 'POST':
        form = IdeasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = IdeasForm()

    data = {
        'form': form,
        'error': error

    }

    return render(request, 'main/createidea.html', data)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
