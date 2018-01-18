from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator

class SignupForm(forms.Form):
    #username = forms.CharField(max_length=100)
    username = forms.EmailField()
    #phone = forms.CharField(validators=[MaxLengthValidator(10),MinLengthValidator(10)])
    password = forms.CharField(widget=forms.PasswordInput())
    #firstname = forms.CharField(max_length=100)
    #lastname = forms.CharField(max_length=100)
    referral = forms.CharField(max_length=15, required=False)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
