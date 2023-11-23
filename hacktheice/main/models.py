from django.db import models


class Aktors(models.Model):
    name = models.CharField(max_length=100, default="Отсутствует")
    intro = models.CharField(max_length=300, default="Отсутствует")
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name

