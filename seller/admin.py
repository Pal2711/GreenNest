from django.contrib import admin
from .models import *

class MainItemAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["name", "img","des"]

admin.site.register(mainitem, MainItemAdmin)


class FirutAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["name", "img", "des"]

admin.site.register(Firut, FirutAdmin)


class VegetablesAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["name", "img", "des"]

admin.site.register(Vegetables, VegetablesAdmin)


class sellproductadmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display=["product","quantity_kg","price_kg","harvest_date","image","contact"]
admin.site.register(sellproduct,sellproductadmin)
