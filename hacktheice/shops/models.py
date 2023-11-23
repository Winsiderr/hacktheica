from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100, default="Отсутствует")
    text = models.TextField(blank=True)
    godnost = models.CharField(max_length=10, default="Отсутствует")
    price = models.IntegerField(default="Отсутствует")
    colvo = models.IntegerField(default="Отсутствует")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.text

class AddedProds(models.Model):
    colvo = models.IntegerField(default=0)
    product = models.OneToOneField(Products, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product.text