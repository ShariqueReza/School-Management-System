from django.contrib import admin
from app.models import teachers,feedback,all_students,Student,all_results,Result,all_exams,Exam,Announcement,Events

# Register your models here.
admin.site.register(teachers)
admin.site.register(feedback)
admin.site.register(all_students)
admin.site.register(Student)
admin.site.register(all_results)
admin.site.register(Result)
admin.site.register(all_exams)
admin.site.register(Exam)
admin.site.register(Announcement)
admin.site.register(Events)

