from django.contrib import admin
from app.models import teachers,feedback,Student

# Register your models here.
admin.site.register(teachers)
admin.site.register(feedback)
admin.site.register(Student)