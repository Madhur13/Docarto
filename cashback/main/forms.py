from django import forms
from django.core.validators import MaxLengthValidator,MinLengthValidator

class BankDetailsForm(forms.Form):
    account_name = forms.CharField(max_length=100)
    account_no = forms.CharField(max_length=50)
    ifsc = forms.CharField(max_length=15)

class PaytmDetailsForm(forms.Form):
    #paytm_name = forms.CharField(max_length=100)
    paytm_no = forms.IntegerField()

class UserSettingsForm(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField(validators=[MaxLengthValidator(10),MinLengthValidator(10)])

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


class BrandAmbassadorForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    fb_url = forms.URLField(required=False)
    profession = forms.IntegerField(required=False)
    why = forms.CharField(max_length=100, required=False)
    how = forms.CharField(max_length=100, required=False)
    interests = forms.CharField(max_length=100, required=False)

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15, required=False)
    email = forms.EmailField(required=False)
    message = forms.CharField(max_length=1000)
