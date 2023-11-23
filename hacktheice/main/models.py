from django.db import models

class NewNews(models.Model):
    name = models.CharField(max_length=100, default="Отсутствует")
    intro = models.CharField(max_length=300, default="Отсутствует")
    text = models.TextField(default="Отсутствует")


    def __str__(self):
        return self.name