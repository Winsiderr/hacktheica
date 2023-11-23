from django.db import models

class Aktors(models.Model):
    name = models.CharField(max_length=100, default="Отсутствует")
    text = models.TextField(blank=True)
