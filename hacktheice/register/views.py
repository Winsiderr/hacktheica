from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import Create
from django.contrib.auth import get_user_model

from .models import CustomUser


@login_required
def profile_view(request):
    return render(request, 'register/index.html')


class Register(FormView):
    model = CustomUser
    form_class = Create
    template_name = 'registration/registration.html'
    success_url = reverse_lazy("register:index")

    def form_valid(self, form):
        form.save()
        form_group = Group.objects.get(name=form.cleaned_data['groups'])
        form.save().groups.add(form_group)
        form.save().save()
        return super().form_valid(form)
