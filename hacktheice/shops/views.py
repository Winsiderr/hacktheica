from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Createprods, InBasck
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
    a = 0
    if request.method == "POST":
        prods = InBasck(request.POST)
        if prods.is_valid():
            prods.save()
    products = AddedProds.objects.all()
    prods = InBasck()
    for i in products:
        a += i.colvo * i.product.price
    data = {
        'prods': prods,
        'prod' : products,
        'a' : a
    }
    return render(request, 'shops/bascket.html', data)