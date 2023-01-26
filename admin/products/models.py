from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    likes = models.PositiveIntegerField(default=0)

class User(models.Model):
    pass