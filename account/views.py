from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User, Todo

from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

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
    todos = Todo.objects.all()
    content = {'todos': todos}
    print(content)
    return render(request, 'user/login.html', content)

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

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('account:login'), {'todos': new_todo})

def deleteTodo(request):
    some_var = request.POST.getlist('checks[]')
    print(some_var)
    dele_todo_id = request.POST.get('todoNum')
    print("삭제한 todo의 id", dele_todo_id)
    todo = Todo.objects.get(id=dele_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('account:login'))

def completeTodo(request):
    com_id = request.POST.get('todoNum')
    todo = Todo.objects.filter(id=com_id)
    print('완료한 todo의 id', com_id, todo)
    if com_id == com_id:
        print('맞아')
    return HttpResponseRedirect(reverse('account:login'))





