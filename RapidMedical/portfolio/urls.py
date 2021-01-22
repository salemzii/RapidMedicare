from django.urls import path
from . import views


urlpatterns=[
    path('', views.welcome, name='welcome'),
    path('proj1/', views.proj1, name='proj1'),
    path('proj2/', views.proj2, name='proj2'),
    path('proj3/', views.proj3, name='proj3'), 
]