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
    
    def clean_username(self):
        username=self.cleaned_data['username'].lower()
        new=User.objects.filter(username=username)
        if new.count():
            raise forms.ValidationError("user already exist")
        return username
    
    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        new=User.objects.filter(email=email)
        if new.count():
            raise forms.ValidationError("Email already exist")
        return email
    
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("password don't match")
        return password2