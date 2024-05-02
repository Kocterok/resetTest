from typing import Any
from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=55)
    anons = models.CharField('Анонс', max_length=250)
    fuel_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'