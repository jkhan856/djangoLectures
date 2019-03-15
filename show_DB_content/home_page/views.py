from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    home_dict = {'greeting':'Welcome!',
                 'instruction':'Go to /users to see the list of users'}
    return(render(request, 'home_page/index.html',context =home_dict))
