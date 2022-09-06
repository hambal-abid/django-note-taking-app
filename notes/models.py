from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='static/',null=True,blank=True)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return self.title