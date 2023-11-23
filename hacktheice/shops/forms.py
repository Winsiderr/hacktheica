from django import forms
from django.forms import ModelForm

from .models import Products


class Createprods(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'text', 'godnost', 'price', 'colvo']
