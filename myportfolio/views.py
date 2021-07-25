from django.shortcuts import render

# Create your views here.
from .models import *
def home(request):
    text = Home.objects.all()

    return render(request, 'myportfolio/index.html',{'text':text})

def contact(request):
    return render(request,'myportfolio/contact.html')

def projects(request):
    project=Project.objects.all()
    return render(request,'myportfolio/projects.html',{'project':project})

def about(request):
    about=About.objects.all()
    return render(request,'myportfolio/about.html',{'about':about})

def certifications(request):
    certi=Certifications.objects.all()
    return render(request,'myportfolio/certi.html',{'certi':certi})

def exp(request):
    exp=WorkExp.objects.all()
    return render(request,'myportfolio/exp.html',{'exp':exp})

def education(request):
    ed=Education.objects.all()
    return render(request,'myportfolio/education.html',{'ed':ed})
