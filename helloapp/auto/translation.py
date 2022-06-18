from modeltranslation.translator import register, TranslationOptions, Translator
from .models import Auto

@register(Auto)
class AutoTranslationOptions(TranslationOptions):
    fields =('description','name')