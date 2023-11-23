from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Createprods
from .models import Products


def products(request):
    prods = Products.objects.all()
    return render(request, 'shops/products.html', {'prods': prods})


def prodsmake(request):
    error = ''
    if request.method == "POST":
        form = Createprods(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('shops/')
        else:
            error = 'ytn'
    form = Createprods()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'shops/makeprods.html', data)

