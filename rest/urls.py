from django.urls import path
from . import views

app_name = "rest"

urlpatterns = [
    path('', views.list, name="list"),
]