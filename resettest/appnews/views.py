from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

def news_home(request):
    news = Articles.objects.order_by('-date')   #[:1]                       # .order_by() метод сортировки
    return render(request, 'appnews/news_home.html', {'news':news})

def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была невалидна'
    
    form = ArticlesForm()
    
    data = {
        'form' : form
    }
    return render(request, 'appnews/create.html', data)