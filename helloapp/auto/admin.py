from django import forms
from django.contrib import admin
from .models import Auto

from modeltranslation.admin import TranslationAdmin
admin.site.register(Auto)
# Register your models here.
class AutoAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label='Описание')
    description_en = forms.CharField(label='Описание')
