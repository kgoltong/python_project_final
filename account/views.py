from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('인증 성공')
            login(request, user)
        else:
            print('인증 실패')
    return render(request, 'user/login.html')

def logout_view(request):
    logout(request)
    return redirect('account:login')

def signup_view(request):

    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        user_id = request.POST.get("user_id")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.last_name = lastname
        user.first_name = firstname
        user.user_id = user_id
        user.save()

        return redirect('account:login')

    return render(request, 'user/signup.html')
