from django import forms
from django.forms import ModelForm

from .models import NewNews


class Createnews(ModelForm):
    class Meta:
        model = NewNews
        fields = ['text', 'intro', 'name']
