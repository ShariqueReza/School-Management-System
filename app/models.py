from django.db import models

# Create your models here.
class teachers(models.Model):
    name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=200,null=True)
    phone_number=models.IntegerField
    subjects=models.CharField(max_length=300,null=True)
    class_teahcer_of=models.IntegerField
    head_of=models.CharField(max_length=200,null=True)

    
