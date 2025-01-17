from django.contrib import admin
from app.models import teachers,feedback,all_students,Student

# Register your models here.
admin.site.register(teachers)
admin.site.register(feedback)
admin.site.register(all_students)
admin.site.register(Student)
