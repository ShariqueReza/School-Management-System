from django.urls import path
from . import views



urlpatterns = [
    path('', views.index_page,name="index"),
    path('Nt_Oc', views.Nt_Oc,name="Nt_Oc"),
    path('teachers', views.teacher_page,name="teacher"),
    path('feedback',views.feedback_page,name="feedback"),
    path('all_student',views.all_student,name="all_student"),
    path('class/<slug:slug>/',views.class_students,name="class_students"), 
    path('get_student/<int:student_id>/', views.get_student, name='get_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('all_results',views.all_result,name="all_result"),
    path('class_results/<slug:slug>/',views.class_results,name="class_results"),
    path('get_result/<int:student_id>/', views.get_result, name='get_result'),
    path('delete_result/<int:student_id>/', views.delete_result, name='delete_result'),
    path('all_exam',views.all_exam,name="all_exam"),
    path('class_exams/<slug:slug>/',views.class_exams,name="class_exams"),
    path('get_exam/<int:student_id>/', views.get_exam, name='get_exam'),
    path('delete_exam/<int:student_id>/', views.delete_exam, name='delete_exam'),
    path('register/', views.register, name='register'),
]