from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.allAdvice, name='allAdvice'),
    path('rand/', views.randAdvice, name='randAdvice'),
]
