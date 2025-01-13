from django.shortcuts import render
from app.models import teachers,feedback
from app.forms import FeedbackForm
from django.http import HttpResponse


# Create your views here.
def index_page(request):
    teacher=teachers.objects.all()
    context={'teacher':teacher}
    return render(request,'app/index.html',context)

def teacher_page(request):
    teacher=teachers.objects.all()
    context={'teacher':teacher}
    return render(request,'app/teachers.html',context)

def feedback_page(request):
    context={}
    return render(request,'app/feedback.html',context)
