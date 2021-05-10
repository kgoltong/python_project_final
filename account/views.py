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


def index(request):
    todos = Todo.objects.all()  # Todo 테이블의 모든 데이터를 가져와서
    content = {'todos': todos}  # 딕셔너리형태로 content에 넣는다
    return render(request, 'my_to_do_app/index.html', content)


def createTodo(request):
    user_input_str = request.POST['todoContent']  # name값이 todoContent였지!
    new_todo = Todo(content=user_input_str)  # DB의 Todo테이블에 쓰고,
    new_todo.save()  # 저장!
    return HttpResponseRedirect(reverse('index'))  # 처리 후 index.html로 돌아가기
# return HttpResponse("create Todo를 할 거야!=>"+user_input_str)

def deleteTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한todo의 id", done_todo_id)
    todo = Todo.objects.get(id=done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))