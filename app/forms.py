from django import forms
from app.models import feedback,Student,Result,Exam

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields={'name','email','comment'}
        widgets = {
             'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'authorName', 'placeholder': 'Enter your name'}),
             'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'gmail', 'placeholder': 'Enter your Email'}), 
             'comment': forms.Textarea(attrs={'class': 'form-control', 'id': 'comment', 'rows': 3, 'placeholder': 'Enter your comment'}), 
            }

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = ['st_name', 'address', 'contact_no', 'parents_names', 'blood_gr', 'emergency']

class ResultForm(forms.ModelForm):
    class Meta:
        model=Result
        fields = ['st_name', 'Math', 'Science', 'English', 'Hindi', 'Total_marks', 'Percentage']

class ExamForm(forms.ModelForm):
    class Meta:
        model=Exam
        fields=['date','subject','shift','start_time','end_time']