import password as password
from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name + ' ' + self.email + ' ' + self.password

class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural='Пользователи'
    ordering = ['-name']