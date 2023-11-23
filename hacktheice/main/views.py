from django.shortcuts import render

from .forms import Createnews
from .models import *


def index(request):
    news = NewNews.objects.all()
    return render(request, 'main/index.html', {'form': news})

def createnews(request):
    if request.method == "POST":
        form = Createnews(request.POST)
        if form.is_valid():
            form.save()
    form = Createnews()

    return render(request, 'main/writenews.html', {'form': form})
