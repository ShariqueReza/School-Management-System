from django.shortcuts import render,redirect
from app.models import teachers,feedback,Student,all_students
from app.forms import FeedbackForm,StudentForm



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
    feedbacks=feedback.objects.all()
    form=FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = FeedbackForm()

    context={'form':form,'feedback':feedbacks}
    return render(request,'app/feedback.html',context)

def all_student(request):
    context={}
    return render(request,'app/all_students.html',context)

def class_students(request,slug):
    class_instance = all_students.objects.get(slug=slug)
    students = Student.objects.filter(class_name=class_instance)

    form=StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = StudentForm()
    context={'students':students,'class_instance': class_instance,'form':form}
    return render(request,'app/students.html',context)

