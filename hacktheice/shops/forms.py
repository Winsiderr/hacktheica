from django import forms
from django.forms import ModelForm

from .models import Products, AddedProds


class Createprods(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'text', 'godnost', 'price', 'colvo']

class InBasck(ModelForm):
    class Meta:
        model = AddedProds
        fields = ['colvo', 'product']