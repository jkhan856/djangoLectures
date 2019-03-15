from django import forms
from users.models import UserInfo

class Register_User (forms.ModelForm):
    #name = forms.CharField()
    #email = forms.EmailField()
    #text = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = UserInfo
        fields = '__all__'
