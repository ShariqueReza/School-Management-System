from django import forms
from app.models import feedback,Student,Result,Exam
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        model = Exam
        fields = ['date', 'subject', 'shift', 'start_time', 'end_time', 'total_time']

class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Type your username....'
        self.fields['email'].widget.attrs['placeholder']='Type your email....'
        self.fields['password1'].widget.attrs['placeholder']='Type your password....'
        self.fields['password2'].widget.attrs['placeholder']='Repeat your password....'