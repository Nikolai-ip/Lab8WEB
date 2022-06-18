from django.db import models

# Create your models here.
from django.urls import reverse


class Auto(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='img/')
    likes = models.BooleanField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('')
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural='Автомобили'