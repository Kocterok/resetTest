from django.urls import path
from . import views

urlpatterns = [
    path('', views.reset),
    path('about', views.about ),
]