from django.shortcuts import render
from django.http import HttpResponse

def reset(request):
    return render(request, 'appreset/index.html')


def about(request):
    return render(request, 'appreset/about.html')
