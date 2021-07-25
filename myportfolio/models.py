from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.
class Home(models.Model):
    text=models.TextField(default='Poojitha')


class About(models.Model):
    image=models.ImageField(upload_to='pic/')
    text=models.TextField(default='Poojitha Ravuri')
    msg=RichTextField()
    url=models.URLField()

class Project(models.Model):
    title=models.CharField(default='project name',max_length=100)
    image=models.ImageField(upload_to='projects/')
    msg = RichTextField()
    url=models.URLField()

    def __str__(self):
        return self.title

class Certifications(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='certis/')
    def __str__(self):
        return self.title

class WorkExp(models.Model):
    cname=models.CharField(max_length=2000)
    start=models.CharField(max_length=100)
    end=models.CharField(max_length=100)
    def __str__(self):
        return self.cname

class Education(models.Model):
    edu=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='edu/')
    clgname=models.CharField(max_length=1000)
    degree=models.CharField(max_length=100)
    years=models.CharField(max_length=100)