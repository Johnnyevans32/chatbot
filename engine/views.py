from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.conf import settings
import requests
import json

import uuid
from django.contrib.auth.views import logout_then_login
import urllib.parse
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import send_mail
# Home page view
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.http import JsonResponse


# Create your views here.
from .models import Bio

def base_layout(request):
    template='home/base.html'
    return render(request, template)

def signup(request):   
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.set_password(password)
            user.save()
            messages.success(request, 'Registration successful')
            return render(request, 'login.html') 
        except Exception as err:
            print(err)
            messages.error(request, 'Something went sideways!')
            return render(request, 'signup.html') 
    return render(request,'signup.html')

def signin(request):   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            else:
                messages.info(request, 'Invalid credentials')
                return render(request, 'login.html') 
        except Exception as err:
            print(err)
            messages.error(request, 'Something went sideways!')
            return render(request, 'login.html') 
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect(reverse('signin'))


@login_required(login_url='signin')
def index(request):
    return render(request, 'chat.html')
