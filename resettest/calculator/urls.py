from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # path('calculater', views.calculater, name='calculater'),
]