from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100, default="Отсутствует")
    text = models.TextField(blank=True)
    godnost = models.CharField(max_length=10, default="Отсутствует")
    price = models.IntegerField(max_length=10, default="Отсутствует")
    colvo = models.IntegerField(max_length=10, default="Отсутствует")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.text