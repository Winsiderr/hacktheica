from django.contrib import admin

from .models import Products, AddedProds

admin.site.register(Products)
admin.site.register(AddedProds)