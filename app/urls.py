from django.urls import path
from . import views



urlpatterns = [
    path('', views.index_page,name="index"),
    path('teachers', views.teacher_page,name="teacher"),
    path('feedback',views.feedback_page,name="feedback"),
    path('all_students',views.all_students,name="all_students"),
]