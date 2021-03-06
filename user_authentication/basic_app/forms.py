from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
from bootstrap_datepicker_plus import DatePickerInput


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta():
        model = UserProfileInfo
        fields = ('date_of_birth', 'profile_pic')
