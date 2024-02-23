from django.urls import path

from . import views

urlpatterns =  [
    path("", MainPage.as_view(), name="main"),
]