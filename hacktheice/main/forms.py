from django import forms
from django.forms import ModelForm

from .models import Aktors


class Createnews(ModelForm):
    class Meta:
        model = Aktors
        fields = ['text', 'intro', 'name']
