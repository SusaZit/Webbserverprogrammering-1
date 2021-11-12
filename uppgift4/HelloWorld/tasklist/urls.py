from django.urls import path
from django.urls import include
from . import views
urlpatterns=[
    path('', views.tasklist, name="tasklist"),
    path('add/', views.add, name="add"),
    path('add.html/', views.add, name="add"),
    path('index.html/', views.tasklist, name="tasklist")
]  
