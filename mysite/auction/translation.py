from .models import Car, Bet
from modeltranslation.translator import TranslationOptions, register


@register(Car)
class ProductTranslationOptions(TranslationOptions):
    fields = ('city', 'country', 'color', 'description')


@register(Bet)
class ProductTranslationOptions(TranslationOptions):
    fields = ('number', 'total_number')
