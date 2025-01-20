from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse,Http404
from app.models import teachers,feedback,Student,all_students,Result,all_results
from app.forms import FeedbackForm,StudentForm,ResultForm



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


#For Student Details
def all_student(request):
    context = {}
    return render(request, 'app/all_students.html', context)

def class_students(request, slug):
    class_instance = get_object_or_404(all_students, slug=slug)
    students = Student.objects.filter(class_name=class_instance)

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if student_id:
            student = Student.objects.get(id=student_id)
            form = StudentForm(request.POST, instance=student)
        else:
            form = StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(f"{request.path_info}?saved=true")
    
    form = StudentForm()
    context = {'students': students, 'class_instance': class_instance, 'form': form}
    return render(request, 'app/students.html', context)


def get_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        data = {
            'id': student.id,
            'st_name': student.st_name,
            'address': student.address,
            'contact_no': student.contact_no,
            'parents_names': student.parents_names,
            'blood_gr': student.blood_gr,
            'emergency': student.emergency,
        }
        return JsonResponse(data)
    except Student.DoesNotExist:
        raise Http404("Student not found")


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return JsonResponse({'status': 'success'})


#For Result Details
def all_result(request):
    context={}
    return render(request, 'app/all_results.html', context)

def class_results(request, slug):
    class_instance = get_object_or_404(all_results, slug=slug)
    results = Result.objects.filter(result_class_name=class_instance)

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if student_id:
            result = Result.objects.get(id=student_id)
            form = ResultForm(request.POST, instance=result)
        else:
            form = ResultForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(f"{request.path_info}?saved=true")
    
    form = ResultForm()
    context = {'results': results, 'class_instance': class_instance, 'form': form}
    return render(request, 'app/result.html', context)

def get_result(request, student_id):
    try:
        result = Result.objects.get(id=student_id)
        data = {
            'id': result.id,
            'st_name': result.st_name,
            'Math': result.Math,
            'Science': result.Science,
            'English': result.English,
            'Hindi': result.Hindi,
            'Total_marks': result.Total_marks,
            'Percentage':result.Percentage
        }
        return JsonResponse(data)
    except Result.DoesNotExist:
        raise Http404("Result not found")