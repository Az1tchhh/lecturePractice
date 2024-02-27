from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *
# Create your views here.

def getUsers(request):
    if request.method == 'GET':
        users = Userr.objects.get_users()
        return render(request, 'users.html', {'users': users})

def createUsers(request):
    if request.method == 'POST':
        form = MyForm(request.POST)