from django.shortcuts import render
from .models import User


# Create your views here.
def register(request):
    return render(request,'register.html')

def userhome(request):
    user_info = User.objects.get(username='testtop')
    return render(request,'userhome.html',{
        'active_menu' : 'user',
        'user_info' : user_info,
    })