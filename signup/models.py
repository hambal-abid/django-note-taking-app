from django.db import models

# Create your models here.
class SignUp(models.Model):
    firstname = models.CharField
    lastname = models.CharField
    username = models.CharField(max_length=20)
    password = models.CharField


class LogIn(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField