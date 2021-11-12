from django.urls import path
from django.urls import include
from . import views
urlpatterns=[
    path('leo/',views.leo, name='cool'),
    path('', views.hello, name="hejsan"),
    path('about.html/', views.about, name="about"),
    path('news.html/', views.news, name="news"),
    path('contact.html/', views.contact, name="contact"),
    
]   
