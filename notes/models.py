from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return self.title