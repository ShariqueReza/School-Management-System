from django.urls import path
from . import views



urlpatterns = [
    path('', views.index_page,name="index"),
    path('teachers', views.teacher_page,name="teacher"),
    path('feedback',views.feedback_page,name="feedback"),
    path('all_student',views.all_student,name="all_student"),
    path('class/<slug:slug>/',views.class_students,name="class_students"), 
    path('get_student/<int:student_id>/', views.get_student, name='get_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('all_results',views.all_result,name="all_result"),
    path('/<slug:slug>/',views.class_results,name="class_results"),
]