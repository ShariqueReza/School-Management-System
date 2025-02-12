from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse,Http404
from app.models import teachers,feedback,Student,all_students,Result,all_results,Exam,all_exams,Notifications,Occasions
from app.forms import FeedbackForm,StudentForm,ResultForm,ExamForm,NewUserForm
from django.contrib.auth import login



# Create your views here.
def index_page(request):
    context={}
    return render(request,'app/index.html',context)

def Nt_Oc(request):
    Notification=Notifications.objects.all().order_by('date')
    Occasion=Occasions.objects.all().order_by('date')
    context={'Notification':Notification,'Occasion':Occasion}
    return render(request,'app/Nt_and_Oc.html',context)

def teacher_page(request):
    teacher=teachers.objects.all()
    context={'teacher':teacher}
    return render(request,'app/teachers.html',context)

def feedback_page(request):
    feedbacks=feedback.objects.all()[0:10]
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
    students = Student.objects.filter(class_name=class_instance).order_by('st_name')

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
    results = Result.objects.filter(result_class_name=class_instance).order_by('-Percentage')

    if request.method == 'POST':
        print(request.POST)
        student_id = request.POST.get('student_id')
        if student_id:
            result = Result.objects.get(id=student_id)
            form = ResultForm(request.POST, instance=result)
        else:
            form = ResultForm(request.POST)
        
        if form.is_valid():
            result = form.save()
            return JsonResponse({
                'status': 'success',
                'id': result.id,
                'st_name': result.st_name,
                'Math': result.Math,
                'Science': result.Science,
                'English': result.English,
                'Hindi': result.Hindi,
                'Total_marks': result.Total_marks,
                'Percentage': result.Percentage
            })

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

def delete_result(request, student_id):
    result = get_object_or_404(Result, id=student_id)
    result.delete()
    return JsonResponse({'status': 'success'})



#for Exam Details

def all_exam(request):
    context = {}
    return render(request, 'app/all_exams.html', context)


def class_exams(request, slug):
    class_instance = get_object_or_404(all_exams, slug=slug)
    exams = Exam.objects.filter(exam_class_name=class_instance).order_by('date')

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if student_id:
            exam = get_object_or_404(Exam, id=student_id)
            form = ExamForm(request.POST, instance=exam)
        else:
            form = ExamForm(request.POST)
        
        if form.is_valid():
            exam = form.save()
            return JsonResponse({
                'status': 'success',
                'id': exam.id,
                'date': exam.date,
                'subject': exam.subject,
                'shift': exam.shift,
                'start_time': exam.start_time,
                'end_time': exam.end_time,
                'total_time': exam.total_time
            })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    form = ExamForm()
    context = {'exams': exams, 'class_instance': class_instance, 'form': form}
    return render(request, 'app/exam.html', context)

def get_exam(request, student_id):
    try:
        exam = Exam.objects.get(id=student_id)
        data = {
            'id': exam.id,
            'date': exam.date,
            'subject': exam.subject,
            'shift': exam.shift,
            'start_time': exam.start_time,
            'end_time': exam.end_time,
            'total_time': exam.total_time

        }
        return JsonResponse(data)
    except Exam.DoesNotExist:
        raise Http404("Exam not found")
    
def delete_exam(request, student_id):
    exam = get_object_or_404(Exam, id=student_id)
    exam.delete()
    return JsonResponse({'status': 'success'})


def register(request):
    form=NewUserForm()

    if request.method == "POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect("/")
        
    context={'form':form}
    return render(request, 'registration/registration.html',context)
