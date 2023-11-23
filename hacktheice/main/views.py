from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'main/index.html')

def Createnews(request):
    return render(request, 'main/writenews.html')