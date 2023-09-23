from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
import uuid
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-user'}),
        }

    def clean(self):
        cd = super().clean()
        email = cd.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email jest już w bazie danych")
        password = cd.get('password')
        password2 = cd.get('password2')
        if password != password2:
            raise forms.ValidationError("Hasła różnią się od siebie")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = str(uuid.uuid4())
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-user'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user'}))
    # remember = forms.BooleanField(label="Zapamiętaj mnie", required=False)
