from django.contrib import admin

# Register your models here.
from .models import Products

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price']

admin.site.register(Products,ProductAdmin)