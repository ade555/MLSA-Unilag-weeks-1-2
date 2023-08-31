from django.urls import path
from .views import hello_world, json

urlpatterns = [
    path("", hello_world, name="he-world"),
    path("content/", json, name="json")
]