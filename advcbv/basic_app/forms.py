from django import forms
from django.contrib.auth.models import User
from basic_app.models import Student

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        #fields = 'Username'
        fields = ('username','email','password')
class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        #fields = '__all__'
        fields = ('school','github','mobile','interest')
