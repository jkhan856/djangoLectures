from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
        my_dict = {'greeting': 'Hello friends! I am from first_app/index.html.'}
        return render(request, 'first_app/index.html', context = my_dict)

def help_page(request):
    help_dict = {'help_message': 'Guys, I need some help learning Django'}
    return render(request, 'help_page/help.html', context = help_dict)
