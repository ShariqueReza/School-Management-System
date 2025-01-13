from django.db import models

# Create your models here.
class teachers(models.Model):
    name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=200,null=True)
    phone_number=models.IntegerField(null=True)
    subjects=models.CharField(max_length=300,null=True)
    class_teacher_of=models.IntegerField(null=True, blank=True)
    position=models.CharField(max_length=200,null=True, blank=True)

class feedback(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,null=True)
    comment=models.CharField(max_length=500)


    
