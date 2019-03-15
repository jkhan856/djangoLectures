from django.shortcuts import render
#from register_user import forms
#from users.models import UserInfo
from register_user.forms import Register_User

def index(request):
    #registration_form = forms.Register_User()
    #register_dict = {'register': 'Enter User details here:',
    #                 'form': registration_form}
    #return render(request, 'register_user/register.html', context = register_dict)
    registration_form = Register_User()
    if request.method == "POST":
        registration_form = Register_User(request.POST)

        if registration_form.is_valid():
            registration_form.save(commit = True)
            return render(request, 'home_page/index.html')
        else:
            print('Error: Form Invalid!')

    return render(request, 'register_user/register.html', context = {'form':registration_form})
