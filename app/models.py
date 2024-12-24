from django.db import models

# Create your models here.
class teachers(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField(max_length=20)
    slug=models.SlugField(max_length=200,unique=True)
