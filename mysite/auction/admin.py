from django.contrib import admin
from .models import Car, Bet
from modeltranslation.translator import TranslationOptions, register
from modeltranslation.admin import TranslationAdmin


@admin.register(Car)
class CarAdmin(TranslationAdmin):

    group_fieldsets = True

    list_display = ("city", "country", "color", "description",)


@admin.register(Bet)
class BetAdmin(TranslationAdmin):

    group_fieldsets = True

    list_display = ("number", 'total_number')
