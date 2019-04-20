from django.urls import path
from . import views

app_name = "rest"

ulrpatterns = [
    path('', views.list, name="list")    
]