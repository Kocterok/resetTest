from django.shortcuts import render
from django.http import HttpResponse

def reset(request):
    data = {
        'title': 'Главная страница',
        'values': ["1", "two", "3", "four", "5"],
        }
    return render(request, 'appreset/index.html', data)


def about(request):
    return render(request, 'appreset/about.html', {'title': 'Про нас'})
