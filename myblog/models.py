from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    redirecturl = models.URLField(max_length=300,blank=True)

    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    #def __str__(self):
    #    return self.title

class TestModel(models.Model):
    username=models.CharField(max_length=25)
    place=models.CharField(max_length=30,blank=True)
    contact=models.CharField(max_length=10,blank=True)

class UserModel(models.Model):
    username=models.CharField(max_length=25)
