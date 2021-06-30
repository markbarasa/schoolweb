from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('course-details/', views.coursedetails, name='coursedetails'),
    path('courses/', views.courses, name='courses'),
    path('events/', views.events, name='events'),
    path('pricing/', views.pricing, name='pricing'),
    path('trainers/', views.trainers, name='trainers'),

 ]