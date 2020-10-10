from newapp.models import ResumeModel
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateResumeForm(ModelForm):
    class Meta:
        model=ResumeModel
        fields="__all__"
        widgets={
            'fullname': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(format=('%d/%m/%Y'),attrs={'class':'form-control', 'type':'date'}),

        }


class ResumeEditForm(ModelForm):
    class Meta:
        model=ResumeModel
        fields="__all__"


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        widgets={
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),

        }



