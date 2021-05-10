from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# AbstractUser를 class User에 상속한다.
class User(AbstractUser):
    user_id = models.CharField(max_length=10)

# todo list 모델
class Todo(models.Model):
    title = models.CharField(max_length=255)