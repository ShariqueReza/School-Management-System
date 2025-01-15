from django.shortcuts import render,redirect
from app.models import teachers,feedback
from app.forms import FeedbackForm



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
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index.html")
        else:
            form = FeedbackForm()
            
    context={'form':form}
    return render(request,'app/feedback.html',context)
