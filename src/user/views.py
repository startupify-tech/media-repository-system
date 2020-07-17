from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def user(request):
    args={'user': request.user}
    {{user}}
    return render(request,'index.html',args)

