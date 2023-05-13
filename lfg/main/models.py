from django.db import models


# Create your models here.
class Hero(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
