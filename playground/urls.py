from django.urls import path
from . import views

urlpatterns = [
    #Mostra Hello Wolrd em /playground/Hello
    path('hello/', views.say_hello)
]