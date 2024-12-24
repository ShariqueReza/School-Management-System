from django.shortcuts import render
from app.models import teachers
from django.http import HttpResponse
# Create your views here.
def index_page(request):
    teacher=teachers.objects.all()
    context={'teacher':teacher}
    return render(request,'app/index.html',context)