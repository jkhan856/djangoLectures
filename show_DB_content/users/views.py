from django.shortcuts import render
from users.models import UserInfo

# Create your views here.
def index(request):
    userList = UserInfo.objects.all()
    user_dict = {'heading': 'Here are your users:',
                 'users': userList}
    return render(request, 'users/users.html', context = user_dict)
