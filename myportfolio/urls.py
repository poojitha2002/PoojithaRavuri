
from . import views
from .views import *
from django.conf.urls import url
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('projects/', views.projects, name='projects'),

path('certifications/', views.certifications, name='certifications'),
path('experience/', views.exp, name='workexp'),
path('contact/', views.contact, name='contact'),
path('education/', views.education, name='education')
    ]