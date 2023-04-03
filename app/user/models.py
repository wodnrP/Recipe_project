from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# user DB모델
class User(AbstractUser):
    profile = models.ImageField(null=True, blank=True)
    nickname = models.CharField(max_length=100, unique=True, null=True)
