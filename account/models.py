from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    birthday = models.DateField('User\'s Birthday')


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='users')
    auth = models.BooleanField('User Is Authenticated')
    contacts = models.ManyToManyField(User, related_name='contacts')
