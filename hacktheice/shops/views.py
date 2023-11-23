from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Createprods
from .models import Products, AddedProds


def products(request):
    prods = Products.objects.all()
    return render(request, 'shops/products.html', {'prods': prods})


def prodsmake(request):
    if request.method == "POST":
        form = Createprods(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../../register/profile/')
    form = Createprods()
    data = {
        'form': form,
    }
    return render(request, 'shops/makeprods.html', data)

def bascket(request):
    prods = AddedProds.objects.all()
    return render(request, 'shops/bascket.html', {'prods': prods})