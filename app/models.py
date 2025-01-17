from django.db import models
from django.utils.text import slugify

# Create your models here.
class teachers(models.Model):
    name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=200,null=True)
    phone_number=models.IntegerField(null=True)
    subjects=models.CharField(max_length=300,null=True)
    class_teacher_of=models.IntegerField(null=True, blank=True)
    position=models.CharField(max_length=200,null=True, blank=True)


class feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,null=True)
    comment=models.CharField(max_length=500)

class all_students(models.Model):
    class_name = models.CharField(max_length=50,blank=True)
    slug=models.SlugField(max_length=200,unique=True,null=True)

    def save(self,*args, **kwargs):
        if not self.id:
            self.slug=slugify(self.class_name)
        return super(all_students,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.class_name


class Student(models.Model):
    class_name = models.ForeignKey(all_students, on_delete=models.CASCADE, related_name='students',null=True,blank=True)
    st_name=models.CharField(max_length=100)
    address=models.CharField(max_length=400)
    contact_no=models.IntegerField(null=True)
    parents_names=models.CharField(max_length=400)
    blood_gr=models.CharField(max_length=10)
    emergency=models.IntegerField(null=True)




    
