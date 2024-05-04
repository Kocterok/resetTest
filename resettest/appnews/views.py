from django.shortcuts import render
from .models import Articles

def news_home(request):
    news = Articles.objects.order_by('-date')   #[:1]                       # .order_by() метод сортировки
    return render(request, 'appnews/news_home.html', {'news':news})