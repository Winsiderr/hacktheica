from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import Group

from .models import *


class Create(UserCreationForm):
    User = get_user_model()
    groups = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("place", "userrole")
