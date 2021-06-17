from django.contrib import admin
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('login/createTodo/', views.createTodo, name='createTodo'),
    path('login/deleteTodo/', views.deleteTodo, name='deleteTodo'),
]

