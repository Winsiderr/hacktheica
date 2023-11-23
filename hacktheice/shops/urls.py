from . import views
from django.urls import path

urlpatterns = [
    path('makeporduscts/', views.prodsmake, name="prods"),
    path('seeporduscts/', views.products, name="prods"),
    path('basket/', views.bascket, name="basck"),
]